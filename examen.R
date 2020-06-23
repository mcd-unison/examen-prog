
library(ggplot2)
library(data.table)

setwd("C:/Users/Laptop/Desktop/examen-prog-master/covid-data")
ep<-read.csv("COVID19MEXICO.csv")                 
head(ep)
Datos=data.frame(ep$FECHA_ACTUALIZACION,ep$FECHA_INGRESO)
head(Datos)
View(Datos)
write.csv(Datos, file="Tabla 1")
