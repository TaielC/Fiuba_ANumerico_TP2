from datos_fijos import *
from math import ceil

def runge_kutta(funcion,h,punto_inicio,punto_fin,valor_inicial, T1=T1_default, T2=T2_default):
	'''funcion es de la forma f(t,y)'''
	resultados = [] # Tuplas de la forma (t,yi)
	resultados.append((punto_inicio,valor_inicial))
	cant_pasos = ceil((punto_fin-punto_inicio)/h)
	
	for i in range(1,cant_pasos+1):
		#Calculo yi+1 en cada iteracion
		yi = resultados[i-1][1]
		ti = resultados[i-1][0]

		k1 = calcular_k1(funcion,ti,yi, T1, T2)
		k2 = calcular_k2(funcion,ti,yi,h,k1, T1, T2)
		k3 = calcular_k3(funcion,ti,yi,h,k2, T1, T2)
		k4 = calcular_k4(funcion,ti,yi,h,k3, T1, T2)

		resultado_actual = yi + (h/6)*(k1+2*k2+2*k3+k4)
		resultados.append((punto_inicio+h*i,resultado_actual))

	return resultados

def calcular_k1(funcion,ti,yi, T1=T1_default, T2=T2_default):
	return funcion(ti,yi,T1,T2)

def calcular_k2(funcion,ti,yi,h,k1, T1=T1_default, T2=T2_default):
	return funcion(ti+h/2,yi+(h/2)*k1,T1,T2)

def calcular_k3(funcion,ti,yi,h,k2, T1=T1_default, T2=T2_default):
	return funcion(ti+h/2,yi+(h/2)*k2,T1,T2)

def calcular_k4(funcion,ti,yi,h,k3, T1=T1_default, T2=T2_default):
	return funcion(ti+h,yi+k3*h,T1,T2)
