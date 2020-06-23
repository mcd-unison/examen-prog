import pandas as reader
import plotly.express as px

df = reader.read_csv('tabla2.csv')

fig = px.bar(df, x='State', y='Value', title='Aggregate cases by special states')
fig.show()
