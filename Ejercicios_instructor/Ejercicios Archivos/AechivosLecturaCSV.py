import csv
while True:
    print ("""\nOpciones que puede realiza\n
1. Leer un archivo csv
""")
    opcion = int (input("Ingrese el numero de la opcion que desea realizar: "))

    if opcion == 1:
        
        def lecturaCsv (nomArchivo):
            try:
                with open (f"C:\\Users\\Sebastian\\OneDrive\\Escritorio\\Clone\\pythontriana\\Ejercicios_instructor\\Ejercicios Archivos\\{nomArchivo}") as archivo:
                    for lectura in archivo:
                        print (lectura)

            except:
                print ("...")

    archivo = input ("Ingrese el nombre del archivo: ")
    lecturaCsv (archivo)

