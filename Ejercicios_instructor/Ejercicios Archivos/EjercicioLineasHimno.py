with open ('C:\\Triana\\pythontriana\\Ejercicios_instructor\\Ejercicios Archivos\\himno.txt', "r+", encoding= "utf-8") as himno:
    cont = 0
    texto = himno.readlines()
    for lineas in himno.readline():
        texto = himno.readline()
    print (texto) 