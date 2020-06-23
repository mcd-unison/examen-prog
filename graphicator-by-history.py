import pandas as reader
import plotly.io as pio

# Read data source.
file_path = 'covid-data/200511COVID19MEXICO.csv'
data = reader.read_csv(file_path, encoding='unicode_escape')
inputDict = data.to_dict(orient='rows')

results = {}
# Process each entry. Populate all data required to go through the data just once.
for entry in inputDict:
    if entry['RESULTADO'] == 1:
        if entry['FECHA_INGRESO'] in results.keys():
            results[entry['FECHA_INGRESO']] += 1
        else:
            results[entry['FECHA_INGRESO']] = 1

sortedResults = {key: results[key] for key in sorted(results)}
print(sortedResults)
graph = dict({
    "data": [{"type": "scatter",
              "x": list(sortedResults.keys()),
              "y": list(sortedResults.values())
              }],
    "layout": {"title": {"text": "Time series of confirmed cases"}}
})
pio.show(graph)
