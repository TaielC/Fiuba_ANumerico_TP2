import numpy as np
from euler import *
from runge_kutta import *
from graficadora import *
from datos_fijos import *


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


def soaking(resultados):
	tf = resultados[-1][0]
	T_arranque = resultados[-1][1] -10
	ti = 0
	n = 1
	temp = 0
	for resultado in resultados:
		if resultado[1] >= T_arranque:
			if ti == 0:
				ti = resultado[0]
			n+=1
			temp+=resultado[1]
	return (tf-ti,temp/n)


def Punto_1():
	punto_inicio = 0 # s
	punto_final = longitud / velocidad # s
	resolucion_euler = euler(funcion_sin_radiacion, cadencia, punto_inicio, punto_final, T_0)
	resolucion_runge_kutta = runge_kutta(funcion_sin_radiacion, cadencia, punto_inicio, punto_final, T_0)
	resultados_reales = calcular_resultados_reales(solucion_sin_radiacion, cadencia, punto_inicio, punto_final)

	guardar_grafico_tiempo_vs_temperatura("Método Euler", resultados_reales, "Solución Analítica", resolucion_euler, "Euler")
	guardar_grafico_tiempo_vs_temperatura("Método Runge-Kutta", resultados_reales, "Solución Analítica", resolucion_runge_kutta, "Runge-Kutta")

	error_relativo_euler = calcular_error_relativo(resultados_reales, resolucion_euler)
	error_relativo_runge_kutta = calcular_error_relativo(resultados_reales, resolucion_runge_kutta)

	guardar_grafico_error_relativo("Error Relativo Euler", error_relativo_euler)
	guardar_grafico_error_relativo("Error Relativo Runge-Kutta", error_relativo_runge_kutta)


def Punto_2():
	punto_inicio = 0 # s
	punto_final = longitud / velocidad # s
	resolucion_runge_kutta = runge_kutta(funcion_completa, cadencia, punto_inicio, punto_final, T_0)

	guardar_grafico_tiempo_vs_temperatura("Resultados obtenidos", resolucion_runge_kutta, "Runge-Kutta")

	resultados_reales_punto_1 = calcular_resultados_reales(solucion_sin_radiacion, cadencia, punto_inicio, punto_final)
	guardar_grafico_tiempo_vs_temperatura("Comparación de Resultados con Solución Analítica Sin Radiación", \
		resolucion_runge_kutta, "Runge-Kutta", resultados_reales_punto_1, "Solución Analítica")

	tiempo_soaking, T_soaking = soaking(resolucion_runge_kutta)
	print(f"Tiempo de Soaking: {tiempo_soaking/60}\n Temperatura Soaking: {T_soaking-273}")


def Punto_3(T1, T2, mostrar=False):
	T1 += 273
	T2 += 273
	punto_inicio = 0 # s
	punto_final = longitud / velocidad # s
	resolucion_runge_kutta = runge_kutta(funcion_completa, cadencia, punto_inicio, punto_final, T_0, T1, T2)
	tiempo_soaking, T_soaking = soaking(resolucion_runge_kutta)
	print(f"Tiempo de Soaking: {tiempo_soaking/60}\n Temperatura Soaking: {T_soaking-273}")
	guardar_grafico_tiempo_vs_temperatura("10 min de Soaking", resolucion_runge_kutta, "Runge-Kutta", mostrar=mostrar)


def duracion_y_temperatura_soaking(T1, T2):
	punto_inicio = 0 # s
	punto_final = longitud / velocidad # s
	resolucion_runge_kutta = runge_kutta(funcion_completa, cadencia, punto_inicio, punto_final, T_0, T1+273, T2+273)
	return soaking(resolucion_runge_kutta)


def F(T1, T2, tiempo_soaking, temperatura_soaking):
	tiempo_soaking_aux, temperatura_soaking_aux = duracion_y_temperatura_soaking(T1, T2)
	return tiempo_soaking_aux-tiempo_soaking, temperatura_soaking_aux-temperatura_soaking


def Punto_5(tiempo_soaking_objetivo, T_soaking_objetivo, semilla=(0,0), n_max=500):

	T12 = np.array(list(semilla))
	objetivo = np.array([T_soaking_objetivo, tiempo_soaking_objetivo])
	abs_tol = 0.5
	J = np.array([[0.25, 0.75], [0.75, 0.25]])

	for i in range(n_max):
		tiempo_soaking, T_soaking = duracion_y_temperatura_soaking(T12[0], T12[1])
		print(f"Tiempo: {tiempo_soaking/60}, Temperatura: {T_soaking-273}")
		F = np.array([T_soaking-273, tiempo_soaking/60]) - objetivo
		K = np.linalg.solve(J, F)
		delta = np.max(np.abs(K))
		print(f'{i+1} {delta} {T12[0]} {T12[1]}')
		T12 = T12 - K
		if delta < abs_tol:
			break
		else:
			if i == n_max-1:
				raise ValueError('No hubo convergencia')
	print(T12[0], T12[1])
