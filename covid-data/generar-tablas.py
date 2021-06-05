'''
Examen de conocimiento de programación e ingeniería de software. (Profr. Waissman, Unison)
El programa lee un archivo CSV de datos de COVID-19 y genera dos tablas CSV y dos gráficas png
Autor: Cayetano Bustamante 
Fecha :  04-06-2021
'''

# Importa librerías 
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


# Lee el archivo CSV y para verificar, imprime en pantalla los primero 5 y úlimos 5 registros de la tabla. 
df = pd.read_csv('200511COVID19MEXICO.csv', encoding = 'ISO-8859-1')
print("\n\n INFORMACIÓN DEL ARCHIVO DE COVID\n")
print(df)


# Crea la Tabla 1, que contiene 3 campos: Fecha de síntomas, Confrimados Sars, Decesos.
dftabla1 = df[df.RESULTADO == 1 ]                           # Selecciona confirmados
dftabla1 = dftabla1[dftabla1.ENTIDAD_UM == 26 ]             # Selecciona sonora
dftabla1 = dftabla1[dftabla1.FECHA_DEF != '9999-99-99' ]    # Selecciona fecha de defunción diferente a 9999
dftabla1 = dftabla1[['FECHA_SINTOMAS','RESULTADO', 'FECHA_DEF']] 
dftabla1.to_csv(r'tabla1.csv', index = False)
print("\n\nINFORMACIÓN DE LA TABLA 1\n")
print(dftabla1)


# Crea la Tabla 2, que contiene la cantidad de casos hospitalizados en
# Sonora, Chihuahua, Nuevo León y Puebla.
dftabla2 = df[['TIPO_PACIENTE','ENTIDAD_UM']]      # Sólo deja 2 campos
dftabla2 = dftabla2[dftabla2.TIPO_PACIENTE == 1 ]  # Selecciona los Hospitalizados 
estados = [26, 8, 19, 21]                          # Selecciona los 4 estados.
dftabla2 = dftabla2[dftabla2['ENTIDAD_UM'].isin(estados)]
# la variable resultado contiene el número de casos por estado.
resultado = dftabla2.groupby('ENTIDAD_UM')['ENTIDAD_UM'].value_counts()
resultado.to_csv(r'tabla2.csv')
print("\n\nINFORMACIÓN DE LA TABLA 2\n")
print(resultado)


# Realizar dos grafica1.png, que consiste en una gráfica de barras con el número de hospitalizados por estado.
x = np.array(["Sonora", "Chihuahua", "Nuevo León", "Puebla"])
y = np.array([1625, 1103, 6837, 2104])
plt.bar(x,y)
plt.savefig('grafica1.png')
print("\n\nSe creó el archivo grafica1.png\n")


# grafica2.png  contiene serie de tiempo de confirmados a nivel nacional.
confirmadosnac = df[['FECHA_SINTOMAS','RESULTADO']] 
confirmadosnac = confirmadosnac[confirmadosnac.RESULTADO == 1 ] 
stiempo = confirmadosnac.groupby('FECHA_SINTOMAS')['RESULTADO'].value_counts().reset_index(name="TOTAL")
fechas  = stiempo.iloc[:,[0]]    # Selecciona las fechas 
total   = stiempo.iloc[:,[2]]    # Selecciona totales.
x = np.array(fechas)
y = np.array(total)
plt.clf()                        # Limpia la meoria de la gráfica anterior.
plt.plot(y, linestyle = 'dotted')
# plt.show()   #  presenta la gráfica en tiempo de ejecución
plt.savefig('grafica2.png')
print("\n\nSe creó el archivo grafica2.png\n")


