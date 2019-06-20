import numpy as np 
import matplotlib.pyplot as plt

def guardar_grafico_tiempo_vs_temperatura(nombre, puntos, puntos2=None, puntos3=None, mostrar=False):
	coordenadas_x = [punto[0]/60 for punto in puntos]
	coordenadas_y = [punto[1]-273 for punto in puntos]
	plt.plot(coordenadas_x,coordenadas_y,'-og')
	if puntos2 is not None:
		plt.plot([p[0]/60 for p in puntos2],[p[1]-273 for p in puntos2],'-or')
	if puntos3 is not None:
		plt.plot([p[0]/60 for p in puntos3],[p[1]-273 for p in puntos3],'-ob')
	plt.xlabel("Tiempo (min)")
	plt.ylabel("Temperatura (⁰C)")
	plt.grid()
	plt.title(nombre)
	plt.savefig(nombre + '.png')
	if mostrar:
		plt.show()
	plt.clf()


def guardar_grafico_error_relativo(nombre, puntos, mostrar=False):
	coordenadas_x = [punto[0]/60 for punto in puntos]
	coordenadas_y = [punto[1]*100 for punto in puntos]
	plt.plot(coordenadas_x,coordenadas_y,'-og')
	plt.xlabel("Tiempo (min)")
	plt.ylabel("Error (%)")
	plt.grid()
	plt.title(nombre)
	plt.savefig(nombre + '.png')
	if mostrar:
		plt.show()
	plt.clf()
