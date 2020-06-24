import numpy
import csv
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime

def CreatecsvFile(data,name):
    myFile = open(name, 'w')
    with myFile:
        writer = csv.writer(myFile)
        writer.writerows(data)

def PlotGrafica1(numeroPacientes):
    estados = ["Sonora", "Chihuahua", "Nuevo Leon", "Puebla"]
    plt.bar(range(4), numeroPacientes, edgecolor='black')

    plt.xticks(range(4), estados, rotation=60)
    plt.title("Numero de casos hospitalizados")
    plt.ylim(0, max(numeroPacientes)+100)
    plt.savefig('grafica1.png')
    plt.show()
    #plt.savefig('grafica1.png')
    

def PlotGrafica2(orderedDates,arrCasos):
    x = orderedDates
    y = arrCasos
    plt.plot(x, y)
    plt.title("Numero total de casos a nivel nacional")
    plt.savefig('grafica2.png')
    plt.show()
    

if __name__ == '__main__':
    #Primero se comienza leer el archivo csv (disculpe la ruta pero apenas asi me funciono)
    with open('C:/Users/Itzel/Desktop/ExamenProgramacion/examen-prog/covid-data/200511COVID19MEXICO.csv', newline='') as File:  
        reader = csv.reader(File)
        fechas = []
        deaths = []
        aux =[]

        sonora = 0
        chihuahua = 0
        nvoLeon = 0
        puebla = 0

        totalDates = []
        #Se comienzan a recorrer las filas
        for row in reader:
            #Esta condicion es para verficar que el paciente se encuentre hospitalizado para el segundo problema
            if(row[9] == '2'):
                #Despues se condicionan los estados de residencia de los pacientes
                if(row[7] == '26'):
                    sonora += 1
                if(row[7] == '08'):
                    chihuahua += 1
                if(row[7] == '19'):
                    nvoLeon += 1
                if(row[7] == '21'):
                    puebla += 1
            #esta condicion es para extraer los registros del estado de sonora y los confirmados con el virus (primer problema)
            if(row[7] == '26' and row[30] == '1'):
                fechas.append(row[11])
                deaths.append(row[12])
                aux.append(row)
            # esta condicion es para verificar los confirmados a nivel nacional y evita agregar un dato extra al arreglo para verificarlo
            if(row[11] != 'FECHA_SINTOMAS' and row[30] == '1'):
                #se agrega a un arreglo todas las fechas donde hubo casos confirmados en el pais
                totalDates.append(row[11])

        #en esta es parte es donde se forma el archivo del segundo problema con los estados y el numero de pacientes hospitalizados
        pacientesHospitalizado = [['Estado','Numero de pacientes hospitalizados'],['Sonora', str(sonora)],["Chihuahua", str(chihuahua)], ["Nuevo León", str(nvoLeon)],["Puebla", str(puebla)]]
        CreatecsvFile(pacientesHospitalizado, 'tabla2.csv')

        #En esta parte se eliminan las fechas repetidas en la lista de pacientes confirmados a nivel nacional
        tDates = list(set(totalDates))
        #Se ordena la misma lista por fecha 
        orderedDates = sorted(
        tDates,
        key=lambda x: datetime.strptime(x,'%Y-%m-%d'), reverse=False
        )
        casosDia = 0
        arrCasos = []
        #Se comparan las fechas para comenzar con la sumatoria de pacientes por fecha
        for i in orderedDates:
            for j in totalDates:
                if(i == j):
                    casosDia += 1
            arrCasos.append(casosDia)
        #Se grafican los datos de fecha y numero de casos por dia
        PlotGrafica2(orderedDates,arrCasos)
        
        #este es para la grafica 1, como ya se tienen el total de pacientes hospitalizados por estado solo se acomodan en un arreglo para graficarse
        numeroPacientes = [sonora, chihuahua, nvoLeon, puebla]
        PlotGrafica1(numeroPacientes)
        
        #En esta parte se obtienen las fechas unicas de la lista de fechas de pacientes confirmados en Sonora
        fechasunicas = list(set(fechas))
        fechasunicasordenadas = sorted(
        fechasunicas,
        key=lambda x: datetime.strptime(x,'%Y-%m-%d'), reverse=False
        )
        acumulados_dia = 0
        deaths_day = 0
        aux_arr = []
        data = [['Fecha', 'Numero_de_casos', 'Numero_de_muertes']]
        for i in fechasunicasordenadas:
            for idx,v in enumerate(fechas):
                #se comparan las fechas para comenzar con el conteo de pacientes confirmados asi como de pacientes muertos
                if(i == v):
                    acumulados_dia += 1
                    if(deaths[idx] != '9999-99-99'):
                        deaths_day += 1
            aux_arr.append(i)
            aux_arr.append(str(acumulados_dia))
            aux_arr.append(str(deaths_day))
            data.append(aux_arr)
            aux_arr = []
            acumulados_dia = 0
            deaths_day = 0
        CreatecsvFile(data, 'tabla1.csv')
        
        
        
        
        
        
    

