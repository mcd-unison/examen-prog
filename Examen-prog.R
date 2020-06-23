#Examen de conocimiento de programación e ingeniería de software
#Enrique Alvarado Ceseña
#Maestria en Ciencia de Datos Unison
#2020-06-23


#Se cargan las librerias a utilizar
library(tidyverse)
library(ggplot2)
library(scales)
library(lubridate)
library(dplyr)


#Leemos la fuente de datos para guardarlo en un objeto data frame
datos_covid <- read.csv("./covid-data/200511COVID19MEXICO.csv",
                         header = TRUE,
                         sep = ",",
                         stringsAsFactors = FALSE)

#Nos aseguramos que las fechas tengan el tipo de dato Date para poder hacer buen manejo de fechas
datos_covid <- datos_covid %>% mutate(FECHA_ACTUALIZACION = as.Date(FECHA_ACTUALIZACION, "%Y-%m-%d"),
                                      FECHA_INGRESO = as.Date(FECHA_INGRESO, "%Y-%m-%d"),
                                      FECHA_SINTOMAS = as.Date(FECHA_SINTOMAS,"%Y-%m-%d"),
                                      FECHA_DEF = as.Date(FECHA_DEF,"%Y-%m-%d")
)

#Separamos Fechas en año, mes, día y semana para poder hacer agrupaciones y visualizaciones
datos_covid <- datos_covid %>% mutate(year_inicio_sintomas = lubridate::year(FECHA_SINTOMAS),
                                      month_inicio_sintomas = lubridate::month(FECHA_SINTOMAS),
                                      day_inicio_sintomas = lubridate::day(FECHA_SINTOMAS),
                                      weekday_inicio_sintomas = weekdays(FECHA_SINTOMAS),
                                      year_deceso = lubridate::year(FECHA_DEF),
                                      month_deceso = lubridate::month(FECHA_DEF),
                                      day_deceso = lubridate::day(FECHA_DEF),
                                      weekday_deceso = weekdays(FECHA_DEF)                                      
)


#Seleccionamos los confirmados de sonora usando filter con los resultados en 1 y entidad de residencia en 26
tabla_1_confirmados_sonora <- 
  (select(datos_covid, ENTIDAD_RES, FECHA_SINTOMAS, RESULTADO, 
          year_inicio_sintomas, month_inicio_sintomas, day_inicio_sintomas
          ) %>%
     group_by(FECHA_SINTOMAS) %>%
     filter(RESULTADO == 1, ENTIDAD_RES == 26)
  
  )

#Hacemos el conteo de los confirmados con el dataframe anterior
tabla_1_confirmados_sonora <- summarise(tabla_1_confirmados_sonora, 
       total_confirmados = n()
       )

#seleccionamos los decesos de los residentes de sonora cuya fecha de defuncion no se NA
tabla_1_decesos_sonora <- 
  (select(datos_covid, ENTIDAD_RES, FECHA_DEF, RESULTADO, 
          year_deceso, month_deceso, day_deceso
  ) %>%
    group_by(FECHA_DEF) %>%
    filter(RESULTADO == 1, ENTIDAD_RES == 26, !is.na(FECHA_DEF))
  )
#Conteo del Data frame anterior
tabla_1_decesos_sonora <- summarise(tabla_1_decesos_sonora, 
                                    total_decesos = n()
)

#Hacemos un Join de las dos tablas anteriores para obtener los confirmados y defunciones por dia
tabla_1 <- tabla_1_confirmados_sonora %>% 
  left_join(tabla_1_decesos_sonora, by = c("FECHA_SINTOMAS" = "FECHA_DEF"))


#Escribimos todo a un csv en el mismo path del csv original
write_csv(tabla_1,"./covid-data/tabla1.csv")

#Generamos DataFrames para los labels de la grafica
CLAVE <- c(26,08,19,21)
NOMBRE <- c('SONORA', 'CHIHUAHUA', 'NUEVO LEON', 'PUEBLA')
estados <- data.frame(CLAVE,NOMBRE)

#Obtenemos los hospitalizados agrupados por fecha de ingreso y entidad, filtrando solo las entidades que queremos
tabla_hospitalizados <- (select(datos_covid, ENTIDAD_RES, FECHA_INGRESO, RESULTADO,
                                year_inicio_sintomas, month_inicio_sintomas, day_inicio_sintomas)
)
#Hacemos un join con el dataframe de estados para incluirlo 
tabla_hospitalizados <- full_join(tabla_hospitalizados, estados, by = c("ENTIDAD_RES" = "CLAVE"))

#Filtramos solo las entidades que requerimos
tabla_hospitalizados <- tabla_hospitalizados %>%
  group_by(FECHA_INGRESO, NOMBRE, ENTIDAD_RES) %>%
  filter(RESULTADO == 1, ENTIDAD_RES == 26 | ENTIDAD_RES == 08 | ENTIDAD_RES == 19 | ENTIDAD_RES == 21) 

#Hacemos el resumen
tabla_hospitalizados <- summarise(tabla_hospitalizados, 
                                  total = n())
#Escribimos todo a un csv en el mismo path del csv original
write_csv(tabla_hospitalizados,"./covid-data/tabla2.csv")
