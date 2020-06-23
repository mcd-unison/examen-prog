import csv

import pandas as reader

# Read data source.
file_path = 'covid-data/200511COVID19MEXICO.csv'
data = reader.read_csv(file_path, encoding='unicode_escape')
inputDict = data.to_dict(orient='rows')

# Constants
SONORA = ('Sonora', 26)
CHIHUAHUA = ('Chihuahua', 8)
NUEVO_LEON = ('Nuevo Leon', 19)
PUEBLA = ('Puebla', 21)
NAME = 0
ID = 1
# Data keys
ENTIDAD_KEY = 'ENTIDAD_UM'

# Result accumulators
sonoraResults = []

# Utility function for requirement for "tabla1"
def isEntryForSonoraResults(entry):
    isFromSonora = entry[ENTIDAD_KEY] == SONORA[1]
    isCovidPositive = entry['RESULTADO'] == 1
    return isFromSonora and isCovidPositive


# Process each entry. Populate all data required to go through the data just once.
for entry in inputDict:
    if isEntryForSonoraResults(entry):
        sonoraResults.append(entry)

# Process Sonora Results
sortedSonoraResults = sorted(sonoraResults, key=lambda r: (r['FECHA_SINTOMAS'], r['FECHA_DEF']))

# Write "tabla1.csv"
with open('tabla1.csv', 'w') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(['Fecha', 'Confirmado', 'Inicio sintomas', 'Deceso', 'Fecha deceso'])
    for entry in sortedSonoraResults:
        row = [entry['FECHA_ACTUALIZACION'],
               'Si' if entry['RESULTADO'] == 1 else 'No',
               entry['FECHA_SINTOMAS'],
               'Si' if entry['FECHA_DEF'] != '9999-99-99' else 'No',
               entry['FECHA_DEF'] if entry['FECHA_DEF'] != '9999-99-99' else '',
               ]
        writer.writerow(row)
