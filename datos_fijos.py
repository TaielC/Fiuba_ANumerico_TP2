from math import pi
from math import e

numero_padron = 102145

# Propiedades del Material
densidad = 7850 # kg/m³
calor_especifico = 480 # J/kgK

# Geometría del Material
diametro = 244.48 * 10**-3 # m
espesor = 13.84 * 10**-3 # m
longitud_tubo = 12 # m

# Geometría del Horno
longitud = 50 # m
n_bols = 50 # cantidad

# Parámetros de Transferencia de Calor
coef_conveccion = 20 # W/m²K
cte_StefanBoltzmann = 5.6703 * 10**-8 # W/m²K
factor_emisividad_tubo = 0.85

# Parámetros del Proceso 
cadencia = int(round( -10 / 10000 * (numero_padron - 90000) + 35 )) # s
T1_default = int(round( 200 / 10000 * (numero_padron - 90000) + 500 )) # K
T2_default = int(round( 200 / 10000 * (numero_padron - 90000) + 500 )) # K
print(T1_default)
print(T2_default)
T1_default += 273
T2_default += 273

# Constantes
area_intercambio_calor = pi * diametro * longitud_tubo
masa = densidad * pi * diametro * espesor * ( 1 - espesor/diametro ) * longitud_tubo
T_0 = 20 + 273.15 # K
velocidad = longitud / (n_bols * cadencia)


def funcion_sin_radiacion(t, T, T1_entorno=T1_default, T2_entorno=T2_default):
	T_entorno = T1_entorno if t * velocidad < longitud//2 else T2_entorno
	return ( coef_conveccion * area_intercambio_calor * ( T - T_entorno ) / ( - masa * calor_especifico ) )


def funcion_completa(t, T, T1_entorno=T1_default, T2_entorno=T2_default):
	T_entorno = T1_entorno if t * velocidad < longitud//2 else T2_entorno
	return ( ( coef_conveccion * area_intercambio_calor * ( T - T_entorno ) + \
			cte_StefanBoltzmann * factor_emisividad_tubo * area_intercambio_calor * (T**4 - T_entorno**4) ) /\
			( - masa * calor_especifico ) )


def solucion_sin_radiacion(t, T1_entorno=T1_default, T2_entorno=T2_default):
	T_entorno = T1_entorno if t * velocidad < longitud//2 else T2_entorno
	return ( T_entorno + (T_0 - T_entorno) * e ** ( - coef_conveccion * area_intercambio_calor * t / ( masa * calor_especifico ) ) )
