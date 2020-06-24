import pandas as pd
pd.set_option('display.max_columns', None)

# Primero cambie los caracteres especiales que impedian la correcta lectura
# Leemos el archivo
dfCovid = pd.read_csv("covid-data/200511COVID19MEXICO.CSV")
dfCovid['FECHA_SINTOMAS'] = dfCovid['FECHA_SINTOMAS'].astype('datetime64[ns]')

# Filtramos los positivos
dfCovidPositivo = dfCovid[dfCovid['RESULTADO'] == 1 ]

# Filtramos por la unidad medica donde se atendio ("Sonora")
dfCovidPositivo = dfCovid[dfCovid['ENTIDAD_UM'] == 26 ]

# Obtenemos todos los positivos con fecha de defuncion diferente de "9999-99-99" 
dfPositivoDef = dfCovidPositivo[dfCovidPositivo["FECHA_DEF"] != "9999-99-99"].copy()
dfPositivoDef["FECHA_DEF"] = pd.to_datetime(dfPositivoDef["FECHA_DEF"])

#Agrupados por "FECHA_DEF" y contamos por "ID_REGISTRO" para obtener el total de defunciones por fecha
dfPositivoDef = dfPositivoDef.groupby("FECHA_DEF").agg({"ID_REGISTRO":"count"}).reset_index()

# Renombramos las columnas
dfPositivoDef.columns = ["FECHA","TOTAL_DEFUNCIONES"]

# Agrupamos por "FECHA_SINTOMAS" y contamos por "ID_REGISTRO" para obtener el total de confirmados por fecha
dfPositivoTotal = dfCovidPositivo.groupby("FECHA_SINTOMAS").agg({"ID_REGISTRO":"count"}).copy().reset_index()

# Renombramos las columnas
dfPositivoTotal.columns = ["FECHA","TOTAL_CONFIRMADOS"]

# Hacemos una mezcla de los dos dataframes para obtener nuestra tabla agrupada por fecha
# con TOTAL_CONFIRMADOS y TOTAL_DEFUNCIONES en SONORA
dfResultFecha = pd.merge(dfPositivoTotal, dfPositivoDef, how='outer', on='FECHA').fillna(0)
dfResultFecha.to_csv("tabla1.csv",index=False)