from datos_fijos import *
from euler import *
from runge_kutta import *
from graficadora import *

def transformar_a_celcius_minutos(resultados):
	resultados_transformados = []
	for i in range(len(resultados)):
		resultados_transformados.append((resultados[i][0]/60, resultados[i][1] - 273.15))
	return resultados_transformados

def calcular_resultados_reales(funcion, h, punto_inicio, punto_final):
	i = punto_inicio
	resultados = []
	while i <= punto_final:
		resultados.append((i, funcion(i)))
		i+=h
	return resultados

def calcular_error_relativo(resultados_reales, resultados):
	lista = []
	for i in range(len(resultados_reales)):
		lista.append((resultados_reales[i][0], abs(resultados_reales[i][1]-resultados[i][1])/resultados_reales[i][1]))
	return lista

def Punto_1():
	punto_inicio = 0 # s
	punto_final = longitud / velocidad # s
	resolucion_euler = euler(funcion_sin_radiacion, cadencia, punto_inicio, punto_final, T_0)
	resolucion_runge_kutta = runge_kutta(funcion_sin_radiacion, cadencia, punto_inicio, punto_final, T_0)
	resultados_reales = calcular_resultados_reales(solucion_sin_radiacion, cadencia, punto_inicio, punto_final)

	guardar_grafico_tiempo_vs_temperatura("Método Euler", resolucion_euler)
	guardar_grafico_tiempo_vs_temperatura("Método Runge-Kutta", resolucion_runge_kutta)
	guardar_grafico_tiempo_vs_temperatura("Comparación de Métodods con Solución Analítica", \
		resultados_reales, resolucion_euler, resolucion_runge_kutta)

	error_relativo_euler = calcular_error_relativo(resultados_reales, resolucion_euler)
	error_relativo_runge_kutta = calcular_error_relativo(resultados_reales, resolucion_runge_kutta)

	guardar_grafico_error_relativo("Error Relativo Euler", error_relativo_euler)
	guardar_grafico_error_relativo("Error Relativo Runge-Kutta", error_relativo_runge_kutta)
