library(epiR)
library(survival)
library(ggplot2)
library(data.table)
names(iris) 
head(iris, n = 4)
summary(iris)
str(iris)
View(iris)
write.csv(iris, file = "iris.csv")

setwd("C:/Users/Laptop/Desktop/examen-prog-master/covid-data")
Covidata <- fread("COVID19MEXICO.csv",select=c("FECHA_ACTUALIZACION","FECHA_INGRESO")
head(Covidata)
ep<-read.csv("COVID19MEXICO.csv")                 
head(ep)
write.csv(Covidata, file = "Covidata.csv")



Datos=data.frame(ep$FECHA_ACTUALIZACION,ep$SEXO[])
head(Datos)
View(Datos)
write.csv(Datos, file="Tabla 1")
