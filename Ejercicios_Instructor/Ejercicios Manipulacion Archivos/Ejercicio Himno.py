# READLINE

# Se le asigna a una variable un directorio con un modo de apertura r (lectura) con encoding= "utf-8" que permite leer caracteres como la ñ etc..
archivo = open ('C:\\Users\\Sebastian\\OneDrive\\Escritorio\\Clone\\pythontriana\\Ejercicios Instructor\\Ejercicios Manipulacion Archivos\\himno.txt', "r", encoding= "utf-8")
# Cont servira como contador de las lineas
cont = 0
# A una valiable se le asigna la variable que contiene el directorio mas el .readline() que funciona para leer solo una linea del texto
linea = archivo.readline ()
# El espacion en blanco se vera solo al final del texto por eso la condicion del bloque while es que cuente cuando la variable que 
# Contiene las lineas del texto sea diferente a un espacion en blanco
while linea != "":
    # Si dicha condicion es verdadera a la variable con se le sumara 1
    cont = cont + 1
    # Se imprimira la linea en la que va la iteracion mas su texto correspondiente
    print (f"{cont}. {linea}")
    # Se llama de nuevo la variable que contiene la linea del archivo mas el archivo.readline() para que este pase de linea
    linea = archivo.readline ()
# Ya cuando se acaba la iteracion se cierra el archivo
archivo.close()

"""-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------"""

# READLINES

# Se le asigna a una variable un directorio con un modo de apertura r (lectura) con encoding= "utf-8" que permite leer caracteres como la ñ etc..
archivo = open ('C:\\Users\\Sebastian\\OneDrive\\Escritorio\\Clone\\pythontriana\\Ejercicios Instructor\\Ejercicios Manipulacion Archivos\\himno.txt', "r", encoding= "utf-8")
# Cont servira como contador de las lineas
cont = 0
# Se crea un bucle for que itere el archivo.readlines() este metodo adiferencia del .readline, cuenta todas las lineas no como el anterior
# Que solo cuanta una sola linea
for linea in archivo.readlines():
    # Cada que se haya una iteracion de de la variable linea que es la que itera archivo.readlines() se cuenta 1 que se tomara como el numero
    # De la linea en la que se va
    cont = cont + 1
    # Y se imprime el numero de linea mas la linea que le corresponde
    print (f"{cont}. {linea}")
# Finalizada la iteracion se cierra el archivo
archivo.close()