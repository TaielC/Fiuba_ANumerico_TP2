from datos_fijos import *
from euler import *
from runge_kutta import *
from graficadora import *

def calcular_resultados_reales(funcion, h, punto_inicio, punto_final):
	i = punto_inicio
	resultados = []
	while i <= punto_final:
		resultados.append((i, funcion(i)))
		i+=h
	return resultados

def calcular_diferencias(resultados, resultados1):
	lista = []
	for i in range(len(resultados)):
		lista.append((resultados[i][0], abs(resultados[i][1]-resultados1[i][1])))
	return lista

def Punto_1():
	punto_inicio = 0 # s
	punto_final = longitud / velocidad # s
	resolucion_euler = euler(funcion_sin_radiacion, cadencia, punto_inicio, punto_final, T_0)
	resolucion_runge_kutta = runge_kutta(funcion_sin_radiacion, cadencia, punto_inicio, punto_final, T_0)
	resultados_reales = calcular_resultados_reales(solucion_sin_radiacion, cadencia, punto_inicio, punto_final)

	graficar(resolucion_euler, resolucion_runge_kutta)

	diferencia_euler = calcular_diferencias(resultados_reales, resolucion_euler)
	diferencia_runge_kutta = calcular_diferencias(resultados_reales, resolucion_runge_kutta)

	graficar(diferencia_euler)
	graficar(diferencia_runge_kutta)