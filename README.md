# Respuesta a examen de programación e ingeniería de software 
A través de este proyecto se podrán obtener información de los casos confirmados a la Covid19 en México utilizando datos antiguos publicados por la Secretaría de Salud Federal.

## Pre-requisitos 📋
Se deberá tener instalado previamente python y los paquetes plotly.express y kaleido. 

## Ejecución del proyecto 🚀
Utilizando el  `script.py` se obtienen dos tablas, `tabla1.csv` y `tabla2.xlsx`. La primera almacena la información de los casos confirmados a la 
Covid19 en el estado de Sonora por fechas en que se iniciaron los síntomas, además de la cantidad de fallecidos que hubo entre estos casos con sus respectivas fechas de defunción. La segunda tabla `tabla2.xlsx`, contendrá la información de los casos hospitalizados en los estados de Sonora, Chihuahua, Nuevo León y Puebla.
La información de esta última tabla se podrá visualizar a través de un gráfico de barras guardado como `grafica1.png`. Por último, se podrá obtener, a través 
de un grafico de línea (`grafica2.png`), la serie de tiempo correspondiente a los casos confirmados a nivel Nacional. Ambos gráficos se generan de manera interactiva
a traves de un navegador si ejecuta el código a través de linea de comando.

```
python script.py
```

## Resultados
Como se muestra a continuación el estado de Puebla resultó ser el de mayor número de hospitalizados entre los estados analizados, en un periodo de tiempo entre junio 
y mayo de 2020. Además, se puede observar que el número de casos confirmados iba en aumento desde el mes de marzo hasta el mes de abril, aunque durante el mes de 
mayo se mantuvo una tendecia a la baja de la cantidad de casos confirmados.

<p align="center">
  <img src="https://github.com/Lay94/examen-prog/blob/master/grafica1.png" width="350" title="hover text">
  <img src="https://github.com/Lay94/examen-prog/blob/master/grafica2.png" width="350" alt="accessibility text">
</p>
