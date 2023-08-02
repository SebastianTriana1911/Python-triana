
archivo = open ('C:\\Triana\\pythontriana\\Ejercicios_instructor\\Ejercicios Archivos\\himno.txt', "r", encoding= "utf-8")
cont = 0
linea = archivo.readline ()
while linea != "":
    cont = cont + 1
    print (f"{cont}. {linea}")
    linea = archivo.readline ()
archivo.close()

archivo = open ('C:\\Triana\\pythontriana\\Ejercicios_instructor\\Ejercicios Archivos\\himno.txt', "r", encoding= "utf-8")
cont = 0
for linea in archivo.readlines():
    cont = cont + 1
    print (f"{cont}. {linea}")
archivo.close()