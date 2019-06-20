import numpy as np 
import matplotlib.pyplot as plt

def graficar(puntos, puntos2=None, puntos3=None):
	coordenadas_x = [punto[0] for punto in puntos]
	coordenadas_y = [punto[1] for punto in puntos]
	plt.plot(coordenadas_x,coordenadas_y,'-og')
	if puntos2 is not None:
		plt.plot([p[0] for p in puntos2],[p[1] for p in puntos2],'-or')
	if puntos3 is not None:
		plt.plot([p[0] for p in puntos3],[p[1] for p in puntos3],'-ob')
	plt.xlabel("Tiempo (s)")
	plt.ylabel("Temperatura (K)")
	plt.grid()
	plt.show()

