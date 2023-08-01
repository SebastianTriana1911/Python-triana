while True:
    print ("""\nOpciones que puede realiza\n
    1. Crear un archivo
    2. Ingresar informacion a un archivo
    3. Ver cuantas lineas contiene un archivo
    4. Leer informacion que contenga un archivo
    5. Salir
    """)
    opcion = int (input("Ingrese el numero de la opcion que desea realizar: "))
    
    if opcion == 1:

        def crearArchivo (nomArchivo):
            try:
                archivo = open (f"C:\\Users\\Sebastian\\OneDrive\\Escritorio\\Clone\\pythontriana\\Ejercicios_instructor\\Ejercicios Archivos\\{nomArchivo}", "x")
                print ("El archivo se creo exitosamente")
                archivo.close ()
            except FileExistsError:
                print ("El archivo ya existe")

        archivo = input("Ingrese el nombre del archivo: ")
        crearArchivo(archivo)

    if opcion == 2:

        def ingresarInfo (nomArchivo):
            try:
                archivo2 = open (f"C:\\Users\\Sebastian\\OneDrive\\Escritorio\\Clone\\pythontriana\\Ejercicios_instructor\\Ejercicios Archivos\\{nomArchivo}", "a")
                cont = 0
                lineas = int(input ("Ingrese cuantos saltos de linea desea realizar: "))
                for i in range (lineas):
                    cont = cont + 1
                    texto = input (f"Ingrese lo que desea añadir en la linea {cont}: ")
                    archivo2.write (f"{texto} \n")
                print ("\nLo que ingreso fue adjuntado al archivo exitosamente")
                archivo2.close()
            except:
                print ("Error en la ejecucion del codigo")

        archivo2 = input ("Ingrese el nombre del archivo donde va a ingresar informacion: ")
        ingresarInfo(archivo2)
        
    if opcion == 3:

        def lineasExistentes (nomArchivo):
            try:
                archivo = open (f"C:\\Users\\Sebastian\\OneDrive\\Escritorio\\Clone\\pythontriana\\Ejercicios_instructor\\Ejercicios Archivos\\{nomArchivo}", "r")
                cont = 0
                for i in archivo.readlines():
                    cont = cont + 1
                print (f"La cantidad de lineas que hay en el texto es de {cont} lineas")
                archivo.close()
            except:
                print ("Error en la ejecucion del codigo")

        archivo3 = input ("Ingrese el nombre del archivo: ")
        lineasExistentes (archivo3)
        
    if opcion == 4:

        def leerArchivo (nomArchivo):
            try:
                archivo = open (f"C:\\Users\\Sebastian\\OneDrive\\Escritorio\\Clone\\pythontriana\\Ejercicios_instructor\\Ejercicios Archivos\\{nomArchivo}", "r")
                for i in archivo:
                    print (i, end = "")
            except FileNotFoundError:
                print ("No existe ningun archivo con ese nombre")

        archivo4 = input ("Ingrese el nombre del archivo: ")
        leerArchivo (archivo4)

    if opcion == 5:
        print ("\nHASTA PRONTO\n")
        break