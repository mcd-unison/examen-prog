### El proyecto se puede correr de dos formas ya sea por jupyter notebook, por terminal el cual general los archivos, la primera opcion es por terminal 

#1. Intalacion necesarias
##installar python en su sistema.
link de referencia
[Intalacion de python ](https://tecnonucleous.com/2018/01/28/como-instalar-pip-para-python-en-windows-mac-y-linux/)

##pipenv -> manejador de depend
`< pip install pipenv >`

##Clonar repositorio
`< git clone repoURL >`

##ingresar a la carpeta e installar dependencias con el comando
`< pipenv install >`

##Corremos el programa
`< pipenv run python proyecto_final.py >`

#2. Archivo jupyter notebook
## Para esta opcion se tiene un archivo con nombre proyecto_final con extension ipynb para abrir en anaconda o colab 
## solo te tiene que agregar la ruta del archivo en el campo del newDataSet y definir la ruta de archivos csv a guardar globaldir
`< 
newDataSet = pd.read_csv('./covid-data/200511COVID19MEXICO.csv')
globaldir= './csv/'
>`


