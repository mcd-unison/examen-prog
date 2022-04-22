import pandas as pd
import plotly.express as px

#Leyendo archivo
data = pd.read_csv('covid-data/200511COVID19MEXICO.csv', encoding = 'unicode_escape')

## Generando tabla con los casos confirmados en Sonora y los respectivos decesos

#Registro de casos positivos a la Covid19 en Sonora
data_Sonora = data[(data['ENTIDAD_UM'] == 26) & (data['RESULTADO'] == 1)]

#Quedandonos solo con los datos de interes
data_Sonora_filtrado = data_Sonora.loc[:,['FECHA_ACTUALIZACION',
                                          'FECHA_SINTOMAS', 'RESULTADO', 'FECHA_DEF']]

#Agregando columna: 0 si no fallecido, 1 si fallecido
data_Sonora_filtrado['CANTIDAD_DEF'] = [0 if FECHA_DEF == "9999-99-99"
                               else 1 for FECHA_DEF in data_Sonora_filtrado['FECHA_DEF']]

#Mostrando la tabla con la cantidad de casos confirmado en Sonora y la cantidad de decesos de los confirmados 
data_Sonora_filtrado = data_Sonora_filtrado.groupby(['FECHA_ACTUALIZACION','FECHA_SINTOMAS', 'FECHA_DEF']).sum()

#Cambiando nombre de columna
data_Sonora_filtrado.rename(columns = {'RESULTADO':'CANTIDAD_CONFIRMADOS'}, inplace = True)

#Guardando en un archivo .csv
data_Sonora_filtrado.to_csv("tabla1.csv")

## Generando tabla con los casos hospitalizados en Sonora, Chihuahua, Nuevo León y Puebla

#Registro de casos hospitalizados a la Covid19 en Sonora, Chihuahua, Nuevo León y Puebla
data_hosp = data[(data['ENTIDAD_UM'].isin([26, 8, 19, 21])) & (data['TIPO_PACIENTE'] == 2)]

#Generando tabla con la cantidad de casos por estado
data_hosp_filtrado = data_hosp.groupby('ENTIDAD_UM').count().loc[:,['ID_REGISTRO']]

#Renombrando columna y sustituyendo los codigos de estado por el nombre
data_hosp_filtrado.rename(columns = {'ID_REGISTRO':'CANTIDAD_HOPITALIZADOS'},
                          index = {26:'Sonora',
                                   8:'Chihuahua',
                                   19:'Nuevo León',
                                   21:'Puebla'},
                          inplace = True)
#Guardando la tabla
data_hosp_filtrado.to_excel("tabla2.xlsx")

## Graficando

fig = px.bar(data_hosp_filtrado, data_hosp_filtrado.index, data_hosp_filtrado.CANTIDAD_HOPITALIZADOS,
            title = "Cantidad de casos hospitalizados por estados")
fig.show()
#Salvando grafico
fig.write_image('grafica1.png')

#Registro de casos confirmados a la Covid19 en Mexico
data_Mexico = data[(data['RESULTADO'] == 1)]
data_Mexico_filtrado = data_hosp.groupby('FECHA_SINTOMAS').count().loc[:,['ID_REGISTRO']]

#Cambiando nombre de columna
data_Mexico_filtrado.rename(columns = {'ID_REGISTRO':'CASOS_CONFIRMADOS'}, inplace = True)

#Graficando serie de tiempo
fig = px.line(data_Mexico_filtrado, data_Mexico_filtrado.index, data_Mexico_filtrado.CASOS_CONFIRMADOS,
            title = "Cantidad de casos confirmados a la Covid19 en Mexico")
fig.show()
#Salvando grafico
fig.write_image('grafica2.png')