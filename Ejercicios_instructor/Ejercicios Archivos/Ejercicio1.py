def crearArchivo (nomArchivo):
    try:
        archivo = open (f"C:\\Triana\\pythontriana\\Ejercicios_instructor\\Ejercicios Archivos\\{nomArchivo}", "x")
        archivo.close ()
    except FileExistsError:
        print ("El archivo ya existe")
        
def ingresarInfo (nomArchivo):
    try:
        archivo = open (f"C:\\Triana\\pythontriana\\Ejercicios_instructor\\Ejercicios Archivos\\{nomArchivo}", "a")
        lineas = int(input ("Ingrese cuantos saltos de linea desea realizar: "))
        for i in range (lineas + 1):
            texto = input ("Ingrese lo que desea añadir en el texto: ")
            archivo.write (f"{texto} \n")
            print ("\nLo que ingreso fue adjuntado al archivo exitosamente")
            archivo.close()
    except:
            print ("El nombre del archivo es incorrecto")
                
while True:
    print ("""\nOpciones que puede realiza\n
    1. Crear un archivo
    2. Ingresar informacion a un archivo
    3. Ver cuantas lineas contiene un archivo
    4. Salir
    """)
    opcion = int (input("Ingrese el numero de la opcion que desea realizar: "))
    
    if opcion == 1:
        archivo = input("Ingrese el nombre del archivo: ")
        crearArchivo(archivo)

    if opcion == 2:
        archivo = input ("Ingrese el nombre del archivo donde va a ingresar informacion: ")
        ingresarInfo(archivo)
        
    if opcion == 3:
        def lineasExistentes (nomArchivo):
            try:
                archivo = open (nomArchivo, "rt")
                cont = 0
                for i in archivo.readlines():
                    cont = cont + 1
                print (f"La cantidad de lineas que hay en el texto es de {cont}")
                archivo.close()
            except:
                print ("...")
        archivo = input ("Ingrese el nombre del archivo: ")
        lineasExistentes (archivo)
        
    if opcion == 4:
        break
