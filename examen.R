#Grecia Mendoza 
library(ggplot2)
library(data.table)
library(dplyr)

#Dirección de trabajo
setwd("C:/Users/Laptop/Desktop/examen-maestria/examen-prog/covid-data")

#Leemos nuestra base de datos covid
covid<-read.csv("200511COVID19MEXICO.csv")

#Tabla 1

#Creamos un subconjunto para seleccionar personas únicamente del estado de Sonora y positivos 
covid1<- subset(covid, ENTIDAD_RES == 26 & RESULTADO==1)

#Creamos un data frame con nuestras variables de interés
Datos<-data.frame(covid1$FECHA_SINTOMAS,covid1$RESULTADO,covid1$FECHA_DEF)

#Función que nos permite guardar nuestra data frame en un archivo csv
write.csv(Datos, file="tabla1.csv")















