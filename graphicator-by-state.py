import pandas as reader
import plotly.express as px

# This script generates a bar view for the aggregate of cases by state (Sonora, Chihuahua, Nuevo Leon, Puebla).
df = reader.read_csv('tabla2.csv')

fig = px.bar(df, x='State', y='Value', title='Aggregate cases by special states')
fig.show()
