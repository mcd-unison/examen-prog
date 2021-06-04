#Importando librerias
import matplotlib as mplt
import pandas as pd
import numpy as np
#Cargando datos en frame
newDataSet = pd.read_csv('./covid-data/200511COVID19MEXICO.csv')
#Variables tabla1 : Sonora 26, Positivo 1,  
entidad = 26;
resultadoCovid = 1
globaldir= './csv/'
nameFileSonoraConf = globaldir+'tabla1.csv'
#PRIMERA PARTE
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
#Grabar tabla.csv
ordenCasosMexico.to_csv(nameFileSonoraConf,index=False)


