#Importando librerias
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
#Cargando datos en frame
newDataSet = pd.read_csv('./covid-data/200511COVID19MEXICO.csv')
#Variables tabla1 : Sonora 26, Positivo 1,  
entidad = 26;
resultadoCovid = 1
globaldir= './csv/'
nameFileSonoraConf = globaldir+'tabla1.csv'

nameFileSonChPbNlConf = globaldir+'tabla2.csv'
entidadesHosp= [26,19,8,21]
tipoPaciente = 2
#----PRIMERA PARTE----
#Filtrado de datos
confirmadosSonora =  pd.DataFrame(newDataSet[(newDataSet['ENTIDAD_RES'] == entidad) & (newDataSet['RESULTADO'] == resultadoCovid)])
#Creacion de nuevo campo Defuncion
confirmadosSonora['DEFUNCION'] = np.where(confirmadosSonora['FECHA_DEF']=='9999-99-99', 0, 1) 
#seleccionando columnas [ENTIDAD_RES,FECHA_SINTOMAS,DEFUNCION]
sonoraConfirmados = pd.DataFrame(confirmadosSonora[['FECHA_SINTOMAS','RESULTADO','DEFUNCION']])
#Agrupor por fecha Sintoma
sonoraAgrupados = sonoraConfirmados.groupby('FECHA_SINTOMAS').sum('DEFUNCION','RESULTADO').reset_index()
#Ordenar por fecha de sintomas
ordenCasosMexico = sonoraAgrupados.sort_values('FECHA_SINTOMAS')
#Cambio de nombre columnas
ordenCasosMexico.columns = ['Fecha Sintomas','Casos','Defunciones']
#Grabar tabla.csv
ordenCasosMexico.to_csv(nameFileSonoraConf,index=False)

#----SEGUNDA PARTE FECHA_INGRESO----
#Filtro por entidades Sonora, Puebla, Nuevo leon, Chihuahua
hospSonChNLPu = pd.DataFrame(newDataSet[ (
    (newDataSet['ENTIDAD_RES'] == entidadesHosp[0]) |
    (newDataSet['ENTIDAD_RES'] == entidadesHosp[1]) |
    (newDataSet['ENTIDAD_RES'] == entidadesHosp[2]) |
    (newDataSet['ENTIDAD_RES'] == entidadesHosp[3]) ) & 
    (
    (newDataSet['FECHA_INGRESO'] != '9999-99-99') & (newDataSet['FECHA_INGRESO'] != '') 
    ) &
    (newDataSet['TIPO_PACIENTE'] == tipoPaciente)
    ])
#Crear frame de Entidad y Tipo
hospEntidades = pd.DataFrame(hospSonChNLPu[['ENTIDAD_RES','TIPO_PACIENTE']])
#Contar por estado 
hospSonChNLPuAgrupados = hospEntidades.groupby('ENTIDAD_RES')['TIPO_PACIENTE'].count().reset_index()
#Remplazando valores por nombre de estado
hospSonChNLPuAgrupados["ENTIDAD_RES"].replace({26: "Sonora", 21: "Puebla",19:"Nuevo Leon", 8:"Chihuahua"}, inplace=True)
#cambio de nombre de columnas
hospSonChNLPuAgrupados.columns = ['Estados','Hospitalizados']
#Crear csv
hospSonChNLPuAgrupados.to_csv(nameFileSonChPbNlConf,index=False)

#PARTE 3 generar graficas
#Grafica1 de barras por estado
Estados = hospSonChNLPuAgrupados['Estados']
Hospitalizados = hospSonChNLPuAgrupados['Hospitalizados']
colorEst=['red', 'green', 'blue', 'gray']
# Tamaño
fig, ax = plt.subplots(figsize =(12, 8))
# Barra horizontal
ax.bar(Estados, Hospitalizados, color=colorEst)
plt.xlabel('Estados')
plt.ylabel('Cantidad')
plt.title = 'Hopitalizados en CH,SON,PUB,NL'
#guarda Grafica 1
plt.savefig('grafica1.png')

#Gragica2 tiempo
#Filtro por confirmado
casosConfirmados = pd.DataFrame(newDataSet[(newDataSet['RESULTADO'] == resultadoCovid)])
#seleccion de fecha y resultados
casosConfirmadosFechaResult = pd.DataFrame(casosConfirmados[['FECHA_INGRESO','RESULTADO']])
#Agrupacion por fecha y contar casos
agruparFechasConfirm = casosConfirmadosFechaResult.groupby('FECHA_INGRESO')['RESULTADO'].count().reset_index()
Ingreso = agruparFechasConfirm['FECHA_INGRESO']
Casos = agruparFechasConfirm['RESULTADO']
#graficacion
fig, ax = plt.subplots(figsize =(28, 10))
# Barra horizontal
ax.plot(Ingreso, Casos)
plt.xticks(rotation=90)
plt.xlabel('Fecha')
plt.ylabel('Casos')
#guarda Grafica 2
plt.savefig('grafica2.png')

