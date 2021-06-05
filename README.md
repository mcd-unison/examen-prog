# IMPORTANTE
Desarrollador: Renán Carrillo Grijalva
Examen de conocimiento de programación e ingeniería de software - Maestria en Ciencia de Datos 2021-2
##### Descripción
El examen esta desarrollado en javascript, por lo tanto solo es necesario tener instalado un navegador web para visualizar el procesamiento del archivo .CSV.

Para ejecutar el sistema es necesario tener internet, ya que las librerias estan siendo importadas por CDN.

##### Ejecucion:
Para poder generar las tablas, los archivos .csv y las imagenes debe ser importado el archivo de "200511COVID19MEXICO.csv" o uno con el mismo formato. Esto se puede realizar al momento de ejecutar el archivo index.html que se encuentra dentro de la carpeta examen-prog/exam/index.html, este archivo puede ser ejecutado abriendolo en un navegador web, ahi mismo aparece un boton para seleccionar un archivo automaticamente se leera y arrojara la informacion deseada.

##### Descripcion:
- Los archivos en .csv se generaran al momento de importar el archivo a leer en este caso "200511COVID19MEXICO.csv".
- Las graficas se pueden descargar con el boton que se agrego, de igual manera se agregaron en la carpeta raiz.



#+title: Examen de conocimiento de programación e ingeniería de software
#+author: Maestría en Ciencia de Datos
#+email: mcd@unison.mx
#+date: Admisión 2020-2
#+html: https://github.com/mcd-unison/examen-prog
#+description: Examen  para la admisión a la /Maestria en Ciencia de Datos/ de la Universidad de Sonora
#+options: h:1 num:t toc:nil
#+LATEX_CLASS_OPTIONS: [letter,11pt]
#+LATEX_HEADER: \usepackage[spanish]{babel}

* Proyecto

 1. Ve a la [[https://github.com/mcd-unison/examen-prog][pagina de =Github= del examen]]
    https://github.com/mcd-unison/examen-prog y realiza un =Fork= en tu cuenta
    propia.

 2. Clona el repositorio en tu computadora para que tengas acceso de forma local.

 3. Para el resto del problema podrás usar el lenguaje de tu preferencia, pero
    todo deberá estár codificado y documentado.

* Lectura y procesamiento de datos

 1. En el repositorio se encuentra el archivo

    =covid-data/200511COVID19MEXICO.csv=

    el cual es un archivo antiguo de la COVID-19 publicado por la Secretaría de
    Salud Federal. Para entender las diferentes columnos se agregan igualmente
    los archivos =Catalogos_0412.xlsx= y el archivo =Descriptores_0419.xlsx=.
    Leer el archivo.

 2. Generar una tabla con 5 columnas:

    1. Fecha

    2. Confirmados de SARS-CoV2 en Sonora por fecha usando la fecha de inicio de síntomas (no acumulados)

    3. Decesos (entre los confirmados) por fecha.

 3. Guardar la tabla como =tabla1.csv=, realizar un /commit/ en el repositorio de GitHub.

 4. Generar una tabla con la cantidad de casos hospitalizados en los estados de
    *Sonora*, *Chihuahua*, *Nuevo León* y *Puebla*.

 5. Guardar la tabla como =tabla2.csv=, realizar un /commit/ en el repositorio de GitHub.

 6. Realizar dos grágicas y guardarlas en el repositorio como =grafica1.png= y
    =grafica2.png=, las cuales contengan lo siguiente:

    1. En =grafica1= realizar una gráfica de barras verticales con el número de
       casos hospitalizados (de acuerdo a nuestro archivo) de los estados de
       *Sonora*, *Chihuahua*, *Nuevo León* y *Puebla*.

    2. En =grafica2= graficar la serie de tiempo de confirmados a nivel Nacional en el tiempo.

 7. Realizar un /commit/ y un /pull request/ del repositorio.

 8. Subir al espacio de /moodle/ los archivos que se requirieron para la
    programación, así como =tabla1.csv=, =tabla2.csv=, =grafica1.png= y =grafica2.png=.



* Aspectos a evaluar

Se tomará en cuenta:

1. La calidad del código realizado.
2. La documentación del código y de los datos.
3. La solución para realizar las tablas y las gráficas solicitadas.
