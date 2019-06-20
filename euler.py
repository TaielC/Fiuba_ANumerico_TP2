def funcion(t,y):
	return y - t**2 + 1

def euler(funcion,h,punto_inicio,punto_fin,valor_inicial):
	'''funcion es de la forma f(t,y)'''
	resultados = [] # Tuplas de la forma (t,yi)
	resultados.append((punto_inicio,valor_inicial))
	cant_pasos = int((punto_fin-punto_inicio)//h)
	
	for i in range(1,cant_pasos+1):
		#Calculo yi+1 en cada iteracion
		yi = resultados[i-1][1]
		ti = resultados[i-1][0]
		resultado_actual = yi + h*funcion(ti,yi)
		resultados.append((punto_inicio+h*i,resultado_actual))

	return resultados