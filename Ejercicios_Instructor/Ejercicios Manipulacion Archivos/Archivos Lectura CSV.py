# Se importa csv para la manipulacion de archivos csv que es un archivo ceparado por ","
import csv
while True:
    # Se crea un menu que permita escoger la lectura de archivos csv
    print ("""\nOpciones que puede realiza\n
1. Leer un archivo csv
""")
    opcion = int (input("Ingrese el numero de la opcion que desea realizar: "))

    if opcion == 1:
        # Se crea un metodo que pida como parametro el nombre del archivo que se desea leer
        def lecturaCsv (nomArchivo):
            try:
                # Se abre el archivo with open y se le pone un alias llamado archivo
                with open (f"C:\\Users\\Sebastian\\OneDrive\\Escritorio\\Clone\\pythontriana\\Ejercicios_instructor\\Ejercicios Archivos\\{nomArchivo}") as archivo:
                    # Se itera el alias que contiene el archivo que se acabo de abrir
                    for lectura in archivo:
                        # Se imprime la variable lectura que es la que lleva la iteracion del
                        # Archivo separado por "," o un archivo normal
                        print (lectura)
            # A cualquier excepcion que tenga el codigo para que no se rompa se imprime algo
            except:
                print ("...")

    archivo = input ("Ingrese el nombre del archivo: ")
    lecturaCsv (archivo)

