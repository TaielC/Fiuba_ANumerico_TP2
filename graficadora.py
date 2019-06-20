import numpy as np 
import matplotlib.pyplot as plt

def graficar(puntos):
	coordenadas_x = [punto[0] for punto in puntos]
	coordenadas_y = [punto[1] for punto in puntos]
	plt.plot(coordenadas_x,coordenadas_y,'-og')
	plt.xlabel("Tiempo")
	plt.ylabel("Temperatura")
	plt.grid()
	plt.show()

graficar([(0,1),(1,2),(2,3),(3,4)])