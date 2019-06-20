def funcion(t,y):
	return y - t**2 + 1


def runge_kutta(funcion,h,punto_inicio,punto_fin,valor_inicial):
	'''funcion es de la forma f(t,y)'''
	resultados = [] # Tuplas de la forma (t,yi)
	resultados.append((punto_inicio,valor_inicial))
	cant_pasos = int((punto_fin-punto_inicio)//h)
	
	for i in range(1,cant_pasos+1):
		#Calculo yi+1 en cada iteracion
		yi = resultados[i-1][1]
		ti = resultados[i-1][0]

		k1 = calcular_k1(funcion,ti,yi)
		k2 = calcular_k2(funcion,ti,yi,h,k1)
		k3 = calcular_k3(funcion,ti,yi,h,k2)
		k4 = calcular_k4(funcion,ti,yi,h,k3)

		resultado_actual = yi + (h/6)*(k1+2*k2+2*k3+k4)
		resultados.append((punto_inicio+h*i,resultado_actual))

	return resultados

def calcular_k1(funcion,ti,yi):
	return funcion(ti,yi)

def calcular_k2(funcion,ti,yi,h,k1):
	return funcion(ti+h/2,yi+(h/2)*k1)

def calcular_k3(funcion,ti,yi,h,k2):
	return funcion(ti+h/2,yi+(h/2)*k2)

def calcular_k4(funcion,ti,yi,h,k3):
	return funcion(ti+h,yi+k3*h)