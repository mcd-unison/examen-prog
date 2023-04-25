# Examen programación

## Maestría en Ciencia de Datos

**Evaluación 2023, aspirantes extranjeros**

Las instrucciones son las siguientes:

1. Ve a la pagina de Github del examen https://github.com/mcd-unison/examen-prog y realiza un *Fork* en tu cuenta propia.

2. Clona el repositorio en tu computadora para que tengas acceso de forma local. Para el resto del problema podrás usar el lenguaje de tu preferencia.

3. En la dirección https://www.gob.mx/salud/documentos/datos-abiertos-152127 se puede consultar el archivo que viene el el apartado *Base de Datos* con los datos de la evolución de COVID en México. 

4. Realiza un programa (o una libreta jupyter) que haga lo siguiente:

  1. Descarga el archivo de datos de COVID. Posiblemente tengas que descargar el diccionario de datos para revisarlo.
  2. Genera una figura con 3 gráficas, las cuales sean la letalidad semanal de COVID a lo largo de la pandemia para México, el estado de Sonora, y el municipio de Hermosillo (en Sonora). Seguramente tendrás que consultar el diccionario de datos que se descarga como archivo independiente del mismo sitio. Guardalo en un archivo llamado `figura.png`.
  3. Genera una tabla con el número de enfermos, el número de decesos y el porcentaje de mujeres por año y por estado. 

En el repositorio se encuentra el archivo
covid-data/200511COVID19MEXICO.csv
el cual es un archivo antiguo de la COVID-19 publicado por la Secretaría de Salud Federal. Para entender las diferentes columnas se agregan igualmente los archivos Catalogos_0412.xlsx y el archivo Descriptores_0419.xlsx.

Leer el archivo csv.
Generar una tabla con 5 columnas:
Fecha
Confirmados de SARS-CoV2 en Sonora por fecha usando la fecha de inicio de síntomas (no acumulados)
Decesos (entre los confirmados) por fecha.
Guardar la tabla como tabla1.csv, realizar un commit en el repositorio de GitHub. El archivo tabla1.csv se va a solicitar subir en el examen.
Generar una tabla con la cantidad de casos hospitalizados en los estados de Sonora, Chihuahua, Nuevo León y Puebla.
Guardar la tabla como tabla2.xlsx, realizar un commit en el repositorio de GitHub. El archivo tabla2.xlsx se va a solicitar subir en el examen.
Realizar dos gráficas y guardarlas en el repositorio como grafica1.png y grafica2.png, las cuales contengan lo siguiente:
En grafica1.png realizar una gráfica de barras verticales con el número de casos hospitalizados (de acuerdo a nuestro archivo) de los estados de Sonora, Chihuahua, Nuevo León y Puebla.
En grafica2.png graficar la serie de tiempo de confirmados a nivel Nacional en el tiempo.
Se va a solicitar subir los archivos grafica1.png y grafica2.png.
Elimina el archivo README.org y agrega un archivo README.md donde se explique que se realiza en el proyecto.
Realizar un commit y un pull request del repositorio.
Se va a solicitar agregar un link al repositorio personal con los cambios realizados.


En la evaluación se tomará en cuenta:

La calidad del código realizado.
La documentación del código y de los datos.
La solución para realizar las tablas y las gráficas solicitadas.
La calidad de las gráficas.


Se requiere de la clave que se les proporcionó por correo electrónico para realizar el examen. 

Cualquier problema, por favor comunicarse con mcd@unison.mx, estaremos pendientes todo el día para contestar a sus inquietudes.

Mucho éxito.
