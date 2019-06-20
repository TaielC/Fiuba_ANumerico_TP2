import numpy as np 
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches


def guardar_grafico_tiempo_vs_temperatura(nombre, puntos1, nombre_puntos1='Func1', puntos2=None, nombre_puntos2='Func2',\
		puntos3=None, nombre_puntos3='Func3', mostrar=False):
	plt.plot([p[0]/60 for p in puntos1],[p[1]-273 for p in puntos1],'-og')
	notaciones = [mpatches.Patch(color='green', label=nombre_puntos1)]
	if puntos2 is not None:
		plt.plot([p[0]/60 for p in puntos2],[p[1]-273 for p in puntos2],'-or')
		notaciones.append(mpatches.Patch(color='red', label=nombre_puntos2))
	if puntos3 is not None:
		plt.plot([p[0]/60 for p in puntos3],[p[1]-273 for p in puntos3],'-ob')
		green_patch = mpatches.Patch(color='blue', label=nombre_puntos3)

	plt.legend(handles=notaciones)

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
