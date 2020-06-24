#LIBRERIAS REQUERIDAS
rm(list = ls())
library(plotROC)
library(pROC)
library(ROCR)
library(ggplot2)
library(foreign)
library(psych)

#LEER BASE DE DATOS
setwd("C:/Users/Daniel Fernandez/Desktop/examen-prog-master/covid-data")

#LECTURA DE DATOS
DatosCov<-read.csv("200511COVID19MEXICO.csv", header = TRUE, sep = ",")
names(DatosCov)

#DATOS EN CASOS CONFRIMADOS EN SONORA
DatosSon<-(DatosCov[DatosCov$ENTIDAD_RES==26&DatosCov$RESULTADO==1,c(12,13,31)])


#EXPORTAR CSV
write.csv(DatosSon, file = "tabla1.csv")

#DATOS HOSPITALIZADOS PARA LOS ESTADOS A NIVEL NACIONAL
Datos<-(DatosCov[DatosCov$TIPO_PACIENTE==2,c(8,10)])
#ELIMINACION DE DATOS PARA OBTENER LOS ESTADOS DE 
#SONORA, CHIHUAHUA, PUEBLA Y NUEVO LEON
Datos1<-(Datos[Datos$ENTIDAD_RES!="32",])
Datos1<-(Datos1[Datos1$ENTIDAD_RES!="31",])
Datos1<-(Datos1[Datos1$ENTIDAD_RES!="30",])
Datos1<-(Datos1[Datos1$ENTIDAD_RES!="29",])
Datos1<-(Datos1[Datos1$ENTIDAD_RES!="28",])
Datos1<-(Datos1[Datos1$ENTIDAD_RES!="27",])
Datos1<-(Datos1[Datos1$ENTIDAD_RES!="25",])
Datos1<-(Datos1[Datos1$ENTIDAD_RES!="24",])
Datos1<-(Datos1[Datos1$ENTIDAD_RES!="23",])
Datos1<-(Datos1[Datos1$ENTIDAD_RES!="22",])
Datos1<-(Datos1[Datos1$ENTIDAD_RES!="20",])
Datos1<-(Datos1[Datos1$ENTIDAD_RES!="18",])
Datos1<-(Datos1[Datos1$ENTIDAD_RES!="17",])
Datos1<-(Datos1[Datos1$ENTIDAD_RES!="16",])
Datos1<-(Datos1[Datos1$ENTIDAD_RES!="15",])
Datos1<-(Datos1[Datos1$ENTIDAD_RES!="14",])
Datos1<-(Datos1[Datos1$ENTIDAD_RES!="13",])
Datos1<-(Datos1[Datos1$ENTIDAD_RES!="12",])
Datos1<-(Datos1[Datos1$ENTIDAD_RES!="11",])
Datos1<-(Datos1[Datos1$ENTIDAD_RES!="10",])
Datos1<-(Datos1[Datos1$ENTIDAD_RES!="9",])
Datos1<-(Datos1[Datos1$ENTIDAD_RES!="7",])
Datos1<-(Datos1[Datos1$ENTIDAD_RES!="6",])
Datos1<-(Datos1[Datos1$ENTIDAD_RES!="5",])
Datos1<-(Datos1[Datos1$ENTIDAD_RES!="4",])
Datos1<-(Datos1[Datos1$ENTIDAD_RES!="3",])
Datos1<-(Datos1[Datos1$ENTIDAD_RES!="2",])
Datos1<-(Datos1[Datos1$ENTIDAD_RES!="1",])

#EXPORTAR TRABLA2 A CSV
write.csv(Datos1, file = "tabla2.csv")

#GRAFICA DE BARRAS DE CASOS HOSPITALIZADOS PARA SONORA, CHIHUAHUA, PUEBLA Y NUEVO LEON
ggplot(data=Datos1, aes(x=ENTIDAD_RES), fill=factor(ENTIDAD_RES)) + 
  geom_bar(position="dodge")

#GRAFICA DE SERIE DE TIEMPO DE CASOS CONFIRMADOS
ggplot(data=DatosCov, aes(x=ENTIDAD_RES), fill=color) +
  geom_bar(data=subset(DatosCov, RESULTADO=="1", position="dodge"))
