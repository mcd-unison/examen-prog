Examen de conocimientos de programación para la Maestría en Ciencia de Datos
============================================================================

Autor: Hugo de Jesús Valenzuela Chaparro
----------------------------------------

23 de junio del 2020
--------------------

Este documento y código es para el examen de conocimientos de
programación de la Maestría en Ciencia de Datos. Convocatoria 2020. Se
trabajará en analisis sobre COVID-19, la enfermedad causada por el nuevo
coronavirus SARS-CoV2, haciendo uso de los datos abiertos de la
Secretaria de Salud Federal con fecha de corte al 11 de mayo del 2020.

El lenguaje de programación utilizado es R en versión 3.6.3, haciendo
uso del entorno de desarrollo integrado (IDE) RStudio especificamente,
con versión 1.2.1335.

When you click the **Knit** button a document will be generated that
includes both content as well as the output of any embedded R code
chunks within the document. You can embed an R code chunk like this:

### Importación y limpieza de los datos

Primeramente, importamos la base de datos (BD) cruda incluyendo todas
las columnas.

``` r
# guardar base de datos (BD) en un objeto de R
BD_raw<- read.csv("/home/hugo/examen-prog/covid-data/200511COVID19MEXICO.csv", header = TRUE, sep = ",")
# NOTA: la ruta del directorio de la BD cambiara dependiendo de donde se corra el codigo
```

Ahora, vamos a reducir la base de datos para quedarnos solamente con las
columnas de Fecha de actualización (de la BD), Fecha de inicio de
síntomas, Fecha de defunción, Estado de residencia y el Resultado a la
prueba de SARS-CoV2. Debe verse como la siguiente tabla

``` r
# columnas a extraer
columnas <- c("FECHA_ACTUALIZACION", "ENTIDAD_RES", "FECHA_SINTOMAS", "FECHA_DEF", "RESULTADO")
BD_1 <- subset(BD_raw, select = columnas) # se extraen las columnas
head(BD_1)
```

    ##   FECHA_ACTUALIZACION ENTIDAD_RES FECHA_SINTOMAS  FECHA_DEF RESULTADO
    ## 1          2020-05-11          27     2020-03-29 9999-99-99         1
    ## 2          2020-05-11          25     2020-03-22 2020-03-29         1
    ## 3          2020-05-11          27     2020-03-18 2020-04-05         1
    ## 4          2020-05-11          25     2020-04-04 2020-04-20         1
    ## 5          2020-05-11          25     2020-04-02 2020-04-23         1
    ## 6          2020-05-11          25     2020-03-31 9999-99-99         1

Se nos pide una tabla de tres columnas: fecha (de actualización),
confirmados de SARS-CoV2 por fecha de síntomas, decesos entre los
confirmados. En específico para el Estado de Sonora. Procedemos a hacer
una filtración de la BD para tener las personas de Sonora confirmadas
con SARS-CoV2 por fecha de síntomas y que lamentablemente fallecieron.

Including Plots
---------------

You can also embed plots, for example:

![](Codigo_Fuente_files/figure-markdown_github/pressure-1.png)

Note that the `echo = FALSE` parameter was added to the code chunk to
prevent printing of the R code that generated the plot.
