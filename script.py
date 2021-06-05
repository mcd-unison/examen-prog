'''
    Este script realiza las tareas especificadas en las instrucciones del examen de conocimiento de
    programación e ingeniería de software que se resumen a continuación:

    Primero, se lee el conjunto de datos del Covid-19 en México proporcionados por la Secretaría
    de Salud (Archivo ./covid-data/200511COVID19MEXICO.csv). A partir de esta información, se 
    realiza lo siguiente:

    1.- Se genera el archivo tabla1.csv que contiene las columnas ['FECHA', 'CONFIRMADOS', 'DECESOS'].
        En éste se pueden consultar el número de casos confirmados y decesos por Covid-19 agrupados
        por fecha de ocurrencia. Para obtener la fecha de un caso confirmado se hace uso de la
        fecha de inicio de síntomas.
    
    2. Se genera el archivo tabla2.csv que contiene las columnas ['ESTADO', 'HOSPITALIZADOS']. En 
       éste se pueden consultar el número de pacientes hospitalizados por Covid-19 en los estados de
       Sonora, Chihuahua, Nuevo León y Puebla.
    
    3.- Se genera una gráfica de barras verticales con el número de casos hospitalizados de los 
        estados de Sonora, Chihuahua Nuevo León y Puebla (grafica1.png).
    
    4.- Se genera una serie de tiempo de los casos confirmados a nivel Nacional (grafica2.png).
'''

# Importamos las librerías necesarias
# Para el manejo de los datos
import pandas as pd 
# Para la graficación
import matplotlib.pyplot as plt
import seaborn as sns

# Leemos en un DataFrame los datos originales
datos_originales = pd.read_csv('./covid-data/200511COVID19MEXICO.csv')

# -------------------- TABLA 1 --------------------

# Filtramos los renglones para quedarnos únicamente con los registros de Covid-19 confirmados en
# Sonora. Esto lo hacemos checando las columnas 'ENTIDAD_RES' que contiene la clave del Estado al 
# que pertenece el registro (Sonora = 26), y la columna 'RESULTADO' que contiene la clave del 
# resultado final al diagnóstico de Covid-19 (Positivo SARS-CoV-2 = 1)
confirmados_sonora = datos_originales[(datos_originales['ENTIDAD_RES'] == 26) & (datos_originales['RESULTADO'] == 1)]
# Nos quedamos únicamente con las columnas que nos interesan ('FECHA_SINTOMAS', 'FECHA_DEF')
confirmados_sonora = confirmados_sonora[['FECHA_SINTOMAS', 'FECHA_DEF']]

# Contamos el número de confirmados agrupándolos por fecha de inicio de síntomas
confirmados_por_fecha = confirmados_sonora['FECHA_SINTOMAS'].value_counts().to_frame().reset_index()
# Renombramos las columnas
confirmados_por_fecha.columns = ['FECHA', 'CONFIRMADOS']

# Contamos el número de decesos agrupándolos por cada fecha de deceso registrada
decesos_por_fecha = confirmados_sonora['FECHA_DEF'].value_counts().to_frame().reset_index()
# Renombramos las columnas
decesos_por_fecha.columns = ['FECHA', 'DECESOS']

# Unimos el conteo de confirmados por fecha y el conteo de decesos por fecha. Cada resultado se 
# encuentra en un DataFrame diferente y se unirán de acuerdo a una columna que tengan en común; 
# dicha columna es la que se llama 'FECHA', además, los ordenamos de menor a mayor de acuerdo a
# las fechas.
tabla_1 = pd.merge(confirmados_por_fecha, decesos_por_fecha, how='outer').sort_values(by=['FECHA'])

# El último registro corresponde a la fecha 9999-99-99 que en realidad no existe y sólo se usa para
# indicar que no se ha registrado una fecha de defunción. Simplemente deshechamos ese renglón.
tabla_1 = tabla_1[:-1]

# Como es posible que no todos los días ocurrieran decesos, entonces esos días, por default, la
# función pd.merge les asignará el valor de 'NaN'. Reemplazamos estos 'NaN' por un cero, pues 
# nos referimos a que ese día no ocurrio deceso alguno.
tabla_1.fillna(0, inplace=True)

# # Guardamos el resultado en un archivo csv
tabla_1.to_csv('tabla1.csv', index=False)



# -------------------- TABLA 2 --------------------
# Filtramos a los casos hospitalizados (columna 'TIPO_PACIENTE' == 2)
datos_hosp = datos_originales[datos_originales['TIPO_PACIENTE'] == 2]

# Nos quedamos únicamente con los registros de Sonora, Chihuahua, Nuevo León y Puebla
# (Sonora --> 'ENTIDAD_RES'=26 ; Chihuahua --> 'ENTIDAD_RES'=08 ; Nuevo León --> 'ENTIDAD_RES'=19 
#  Puebla --> 'ENTIDAD_RES'=21).
datos_hosp = datos_hosp[(datos_hosp['ENTIDAD_RES'] == 26) | (datos_hosp['ENTIDAD_RES'] == 8) | 
                        (datos_hosp['ENTIDAD_RES'] == 19) | (datos_hosp['ENTIDAD_RES'] == 21)]

# Reemplazamos los valores de las claves de entidad por el nombre real de los estados
datos_hosp['ENTIDAD_RES'] = datos_hosp['ENTIDAD_RES'].map({26:'Sonora', 8:'Chihuahua', 
                                                           19:'Nuevo León', 21:'Puebla'})
# Contamos la ocurrencia de cada estado en la columna 'ENTIDAD_RES' y guardamos el resultado en un
# dataframe diferente con las columnas 'ESTADO' y 'HOSPITALIZADOS'
tabla_2 = datos_hosp['ENTIDAD_RES'].value_counts().to_frame().reset_index()
tabla_2.columns=['ESTADO', 'HOSPITALIZADOS']

# # Guardamos los restulados en un archivo csv
tabla_2.to_csv('tabla2.csv', index=False)


# -------------------- GRÁFICA 1 --------------------
# Ponemos un fondo oscuro
sns.set()
# Especificamos el tamaño de la gráfica
plt.figure(figsize=(18,12))

# Creamos una gráfica de barras horizontal
plot1 = sns.barplot(x=tabla_2['ESTADO'], y=tabla_2['HOSPITALIZADOS'], palette='Greens_r')
# Indicamos, en cada barra, su valor exacto
for index, row in tabla_2.iterrows():
    plot1.text(row.name, row.HOSPITALIZADOS, round(row.HOSPITALIZADOS, 2), color='black')

# Escribimos el título de la gráfica
plt.title('Número de pacientes hospitalizados por SARS-CoV-2 en los estados de Nuevo León, Puebla, Sonora y Chihuahua', size=20)
# Escribimos las leyendas de los ejes
plot1.set_xlabel("Estado",fontsize=15)
plot1.set_ylabel("Número de pacientes hospitalizados",fontsize=15)

# Guardamos la gráfica 
plt.savefig('grafica1.png', dpi=300)


# -------------------- GRÁFICA 2 --------------------
# Comenzamos obteniendo los registros de los casos confirmados de Covid-19 en todo México
# (columna 'RESULTADO' = 1)
confirmados = datos_originales[datos_originales['RESULTADO'] == 1]

# Contamos el número de confirmados agrupándolos por fecha de inicio de síntomas
confirmados_mexico = confirmados['FECHA_SINTOMAS'].value_counts().to_frame().reset_index()
# Renombramos las columnas
confirmados_mexico.columns = ['FECHA', 'CONFIRMADOS']
# Ordenamos de menor a mayor de acuerdo a la fecha
confirmados_mexico = confirmados_mexico.sort_values(by=['FECHA'])

# Ponemos un fondo oscuro
sns.set()
# Especificamos el tamaño de la gráfica
plt.figure(figsize=(20,10))

# Creamos la serie de tiempo de confirmados
plot2 = sns.lineplot(x=confirmados_mexico['FECHA'], y=confirmados_mexico['CONFIRMADOS'], palette="Dark2")
# Rotamos 90% las fechas en el eje X para que no se impriman unas arriba de otras
plt.xticks(plt.xticks()[0], confirmados_mexico['FECHA'], rotation=90)

# Escribimos el título de la gráfica
plt.title('Número de casos confirmados de SARS-CoV-2 por día a nivel Nacional (México)', size=30)
# Escribimos las leyendas de los ejes
plot2.set_ylabel("Número de casos confirmados",fontsize=15)
plot2.set_xlabel("Fecha",fontsize=15)
# Modificamos el tamaño de los "parámetros" para que las fechas se acomoden bien
plot2.tick_params(labelsize=8)

# Guardamos la gráfica 
plt.savefig('grafica2.png', dpi=300)
