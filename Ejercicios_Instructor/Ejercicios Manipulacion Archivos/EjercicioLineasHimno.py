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

# Se crea un archivo que reciba caracteres "Especiales" como la ñ, con encoding= "utf-8"
with open ('C:\\Users\\Sebastian\\OneDrive\\Escritorio\\Clone\\pythontriana\\Ejercicios_instructor\\Ejercicios Archivos\\resultado.txt', "a", encoding= "utf-8") as stream:
    # Cont permitira contar la linea en la que va la iteraccion
    cont=0
    # Se itera la lista la cual contiene el numero de caracteres de cada linea
    for i in lista:
        # Por cada iteraccion a cont se le suma 1, significa que cuanta la siguiente linea
        cont = cont + 1
        # A una variable se le pasa el texto que muestre el numero de linea y la cantidad de caracteres que tenga dicha linea
        cadena = f"En el verso {cont} hubo {i} caracteres \n"
        # Al alias con el que se guardo el archivo se le pasa el .write() que es para enviar algun tipo de dato al texto previamente creado 
        # Y se le pasa como parametro la variable que contenga lo que se desea escribir en el texto o se le pasa el texto escrito desde el parametro
        stream.write(str(cadena))