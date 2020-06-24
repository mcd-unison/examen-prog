import pandas as pd
pd.set_option('display.max_columns', None)
# Primero cambie los caracteres especiales que impedian la correcta lectura
# Leemos el archivo
dfCovid = pd.read_csv("covid-data/200511COVID19MEXICO.CSV")

# Filtramos los positivos y hospitalizados
dfCovidPositivo = dfCovid.query('RESULTADO == 1 & TIPO_PACIENTE == 2')

# Filtramos por las unidades medicas donde se atendio ("Sonora","Chihuahua","Nuevo Leon","Puebla")
dfCovidPositivo = dfCovid.query('ENTIDAD_UM == 26 | ENTIDAD_UM == 8 | ENTIDAD_UM == 19 | ENTIDAD_UM == 21')

#Agrupados por "ENTIDAD_UM" y contamos por "ID_REGISTRO" para obtener el total de casos
dfCovidPositivoEstados = dfCovidPositivo.groupby("ENTIDAD_UM").agg({"ID_REGISTRO":"count"}).reset_index()

# Renombramos las columnas
dfCovidPositivoEstados.columns = ["ENTIDAD_UM","TOTAL_HOSPITALIZADOS"]

# Agregamos el nombre de la entidad para una mejor referencia
dfCovidPositivoEstados["ENTIDAD"] = ['Chihuahua','Nuevo Leon','Puebla','Sonora']
dfCovidPositivoEstados.to_csv("tabla2.csv",index=False)