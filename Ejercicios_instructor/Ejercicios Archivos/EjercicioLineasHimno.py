# El primer for recorre cada linea del himno para que el segundo solo recorra la frase de la linea en la que vaya el primer for, y cuenta un caracter si este no es un 
# espacion o un salto de linea para luego guardarlo en una lista cada uno de los resultados
with open ('C:\\Users\\Sebastian\\OneDrive\\Escritorio\\Clone\\pythontriana\\Ejercicios_instructor\\Ejercicios Archivos\\himno.txt', "rt", encoding= "utf-8") as himno:
    lista = []
    contChar = 0
    for line in himno:
        for char in line:
            if char != " " and char != "\n":
                contChar = contChar + 1
            else:
                continue
        lista.append(contChar)
        contChar = 0 

with open ('C:\\Users\\Sebastian\\OneDrive\\Escritorio\\Clone\\pythontriana\\Ejercicios_instructor\\Ejercicios Archivos\\resultado.txt', "a", encoding= "utf-8") as stream:
    cont=0
    for i in lista:
        cont = cont + 1
        cadena = f"En el verso {cont} hubo {i} caracteres \n"
        stream.write(str(cadena))