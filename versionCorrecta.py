#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
TP2 ANALISIS NUMERICO
Resolucion de ODE

1 Cuatrimestre 2019

NOTA: Se usan variables y constantes con letras mayusculas y minusculas
para coincidencia con el enunciado. No es practica recomendada en Python.

Por:
Ignacio

"""

#Imports
import numpy as np #Manejo de arrays
import matplotlib.pylab as plt #Rutinas gráficas
from scipy.integrate import odeint #solver de ecuaciones diferenciales
from scipy.integrate import trapz #solver de ecuaciones diferenciales

#Constantes (unidades mks)
NP = 100000. #Padron
rho = 7850. #kg/m3
C = 480. #J/(kg*K)
OD = 0.24448 #m
WT = 0.01384 #m
L_t = 12.0 #m
L = 50 #m
n_bol = 50 #unidades o pasos
cad = np.round(-10 / 10000 * (NP-90000) + 35, 0) #s
Tk = 273.15
T_0 = 20. + Tk #K
h_c = 20. #W/(m**2 * K)
sigma = 5.6703e-8 #W/(m**2 * K**4)
eps = 0.85 #
m = rho * np.pi * OD * WT * (1-WT/OD) * L_t #kg
S = np.pi * OD * L_t #m**2
v_0 = L / (n_bol * cad) #m/s

print('Datos calculados: ')
print('m [kg] = ' +str(m))
print('S [m2] = ' +str(S))
print('v_0 [m/s] = ' +str(v_0))

#Objetivos:
Sk_obj = 10. #minutos
T_Sk_obj = 700 #C

def salida_horno(T_1, T_2, graph=False):
    #Temperatura en el horno
    def T_inf(x):
        if x <= L/2:
            return T_1
        else:
            return T_2

    def f(t, T):
        """
        dT/dt = f(t, T)
        
        CUIDADO - Usa constantes globales
        """
        x = t * v_0 #aproximacion continua, se mueve de a pasitos en realidad
        dT_dt = -1 / (m*C) * ( h_c * S * (T - T_inf(x)) + 
                               sigma * eps * S * (T**4 - T_inf(x)**4) )
        return dT_dt

    #Algoritmos para resolver ODES
    def rk2(f, t0, tf, y0, n_steps=50, verb=False, printk=False):
        """
        Resuelve y' = f(t, y) por RK2
        y(t) puede ser escalar o vectorial, el algoritmo toma la dimension
        del valor inicial y0
        
        Input:
            f: funcion f(t,y) = y'
            to: tiempo inicial (float)
            tf: tiempo final (float)
            y0: valor inicial de y (float o np.array de floats)
            n_steps: cantidad de pasos (entero, el algoritmo calcula el paso h)
        
        Output:
            t: np.array (vector) con los tiempos donde se calcula la solucion
            w: np.array (vector columna o matriz) con la sol numerica para y
        """
        try:
            n_dim = len(np.array(y0))
        except TypeError:
            n_dim = 1
        h = (tf-t0)/n_steps
        t = t0 + h * np.arange(n_steps+1) #vector tiempos
        w = np.zeros([n_steps+1, n_dim])  #solucion inicializa en ceros
        w[0] = y0
        for i in range(n_steps):
            k1 = h * f(t[i], w[i])
            k2 = h * f(t[i] + 0.5*h, w[i] + 0.5*k1)
            #k3 = h * f(t[i] + 0.5*h, w[i] + 0.5*k2)
            #k4 = h * f(t[i+1], w[i] + k3)
            w[i+1] = w[i] + (k2)
            #w[i+1] = w[i] + (k1 + 2*k2 + 2*k3 +k4)/6
            if printk:
                print('Paso ' + str(i))
                print ('k1 = ' + str(k1))
                print ('k2 = ' + str(k2))
                #print ('k3 = ' + str(k3))
                #print ('k4 = ' + str(k4))
        if verb:
            print(np.column_stack([t,w]))
        return t, w

    #Parametros para correr el algoritmo
    t0 = 0. #tiempo inicial
    tf = n_bol * cad #tiempo final
    #si h = cad, entonces n_steps = (tf-t0)/ h = n_bol*cad/cad = n_bol
    n_steps = n_bol * 20
    #Elegir entre metodos RK4 y ODEINT
    #tt, TT_rk4 = rk4(f, t0, tf, T_0, n_steps = n_steps)
    tt = np.linspace(t0, tf, n_steps+1)
    TT = odeint(lambda t, T: f(T,t), T_0, tt)
    
    #Grafica de las funciones
    #Ver https://matplotlib.org
    if graph:
        plt.figure(figsize=(10,7))
        plt.plot(tt/60, TT-Tk, 'o--', lw=1, label='Sol numerica')
        plt.legend(loc='best')
        plt.xlabel('t [min]')
        plt.ylabel('T [C]')
        plt.title('Temperatura de la barra')
        plt.grid(True)
        nombre = 'figura'
        plt.savefig(nombre + '.png')
        plt.show()

    #Calculos posteriores
    T_F = TT[-1]
    Sk_array = tt.reshape(TT.shape)[TT >= T_F - 10]
    Sk_min = (Sk_array[-1] - Sk_array[0]) / 60
    T_Sk_array = TT[TT >= T_F - 10]
    T_Sk = trapz(T_Sk_array)/(T_Sk_array.size-1) #mas preciso que T_Sk_array.mean()
    T_Sk_cel = T_Sk - 273.15
    
    #Parametros de salida
    Sk_min = (Sk_array[-1] - Sk_array[0]) / 60
    T_Sk_cel = T_Sk - 273.15
    
    return T_Sk_cel, Sk_min


print('Objetivos: ')
print('Sk_obj [min]= ' + str(Sk_obj))
print('T_Sk_obj [C]= ' + str(T_Sk_obj))

print('')
print('Corrida de programa principal, probando valores de T_1 y T_2')
T12 = np.array([764., 677.]) + Tk #K
T_Sk, Sk = salida_horno(T12[0], T12[1], graph=True)
print('T_1 [C] = ' +str(T12[0]-Tk))
print('T_2 [C] = ' +str(T12[1]-Tk))
print('Sk [min] = ' + str(Sk))
print('T_sk [C] = ' + str(T_Sk))

print('')
print('Buscando T_1 y T_2 numericamente para lograr objetivos')
n_max = 50
obj = np.array([T_Sk_obj, Sk_obj])
abs_tol = .5
for i in range(n_max):
    J = np.array([[0.25, 0.75], 
                  [0.75, 0.25]])
    F = np.array(salida_horno(*T12)) - obj
    #print('{0:4} {1: .7f} {2: .7f}'.format(i+1, F[0], F[1]))
    K = np.linalg.solve(J, F)
    #print('{0:4} {1: .7f} {2: .7f}'.format(i+1, K[0], K[1]))
    T12_new = T12 - K
    delta = np.max(np.abs(K))
    T12 = T12_new
    print('{0:4} {1: .7f} {2: .7f} {3: .7f}'.format(i+1, delta, T12[0], T12[1]))
    if delta < abs_tol:
        break
    else:
        if i == n_max:
            raise ValueError('No hubo convergencia')
            
Tsk, Sk = salida_horno(T12[0], T12[1], graph=True)
print('T_1 [C] = ' +str(T12[0]-Tk))
print('T_2 [C] = ' +str(T12[1]-Tk))
print('Sk [min] = ' + str(Sk))
print('T_sk [C] = ' + str(T_Sk))
