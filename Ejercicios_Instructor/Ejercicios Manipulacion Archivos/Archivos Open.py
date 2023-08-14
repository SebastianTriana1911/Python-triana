# Se crea un menu con diferentes opciones, para la manipulacion de archivos
while True:
    print ("""\nOpciones que puede realiza\n
    1. Crear un archivo
    2. Ingresar informacion a un archivo
    3. Ver cuantas lineas contiene un archivo
    4. Leer informacion que contenga un archivo
    5. Crear archivo de datos personales
    6. Contar caracteres de un archivo
    7. Salir
    """)
    opcion = int (input("Ingrese el numero de la opcion que desea realizar: "))
    
    if opcion == 1:
        # Se crea una funcion que se pasa como parametro el nombre del archivo que se desea crear 
        # Y dentro ya contiene la ruta del lugar en el que se va a crear, seguido del modo de apertura
        # X que es el que permite crear archivos no existente y si existe genera un error 
        def crearArchivo (nomArchivo):
            try:
                archivo = open (f"C:\\Users\\Sebastian\\OneDrive\\Escritorio\\Clone\\pythontriana\\Ejercicios_instructor\\Ejercicios Archivos\\{nomArchivo}", "x")
                print ("El archivo se creo exitosamente")
                # Se cierra el archivo con el metodo .close ya que no se seguira utilizando en el metodo
                archivo.close ()
                # Si se intenta crear un archivo que ya existe en el mismo directorio saldra un error de 
                # FileExistsError y para eso se antepuso con un except 
            except FileExistsError:
                print ("El archivo ya existe")

        archivo = input("Ingrese el nombre del archivo: ")
        crearArchivo(archivo)

    if opcion == 2:
        
        # Se crea un metodo para ingresar informacion a un archivo y para esto se pasa como parametro el nombre del archivo que se desea manipular
        def ingresarInfo (nomArchivo):
            try:
                # Se abre el archivo con el modo de apertura a que es el que permite insertar informacion al final del archivo que se quiera manipular
                archivo2 = open (f"C:\\Users\\Sebastian\\OneDrive\\Escritorio\\Clone\\pythontriana\\Ejercicios_instructor\\Ejercicios Archivos\\{nomArchivo}", "a")
                # Cont servira para contar la cantidad de lineas que va en el archivo
                cont = 0
                # Se solicita el numero de lineas que va a tener el archivo 
                lineas = int(input ("Ingrese cuantos saltos de linea desea realizar: "))
                # Si en numero de lineas es menor a 0 se lansa una excepcion ya que no se pueden escribir una cantidad de lineas negativas
                if lineas < 0:
                    raise Exception
                # Y si es mayor re itera las lineas que deseo el usuario 
                else: 
                    for i in range (lineas):
                        cont = cont + 1
                        texto = input (f"Ingrese lo que desea añadir en la linea {cont}: ")
                        # Al nombre del se le pasa el .write y se le pasa como parametro la variable que contiene el texto que ingreso el usuario
                        # En la iteracion que se vaya
                        archivo2.write (f"{texto} \n")
                    print ("\nLo que ingreso fue adjuntado al archivo exitosamente")
                    # Luego de haberse insertado el texto se cierra el archivo con el .close ya que no se seguira utilizando
                    archivo2.close()
            # Se crean las excepciones necesarias para los errores que se puedan presentar dentro del codigo 
            except Exception:
                print ("Tiene que ingresar un numero y que sea mayor de 0")
            except:
                print ("Error en la ejecucion del codigo")

        archivo2 = input ("Ingrese el nombre del archivo donde va a ingresar informacion: ")
        ingresarInfo(archivo2)
        
    if opcion == 3:

        def lineasExistentes (nomArchivo):
            try:
                # Se abre un archivo con el modo de apertura r que permite abrir el archivo solo en modo lectura
                archivo = open (f"C:\\Users\\Sebastian\\OneDrive\\Escritorio\\Clone\\pythontriana\\Ejercicios_instructor\\Ejercicios Archivos\\{nomArchivo}", "r")
                cont = 0
                # Al la variable archivo que es la que contiene el archivo a manipular se le pasa el metodo .readlines() que es la que
                # Permite contar todas las lineas que contenga el archivo que se esta manipulando
                for i in archivo.readlines():
                    # Para llevar el contador de dichas lineas se crea un contador que vaya sumando por cada iteracion que vaya teniendo
                    # El archivo con el metodo .readlines()
                    cont = cont + 1
                print (f"La cantidad de lineas que hay en el texto es de {cont} lineas")
                # Se cierra el archivo
                archivo.close()
            # Se crea una excepcion por si se genera algun error en el codigo y este no se rompa
            except:
                print ("Error en la ejecucion del codigo")

        archivo3 = input ("Ingrese el nombre del archivo: ")
        lineasExistentes (archivo3)
        
    if opcion == 4:

        def leerArchivo (nomArchivo):
            try:
                # Se abre nuevamente un archivo en modo de apertura de lectra
                archivo = open (f"C:\\Users\\Sebastian\\OneDrive\\Escritorio\\Clone\\pythontriana\\Ejercicios_instructor\\Ejercicios Archivos\\{nomArchivo}", "r")
                # Se itera el archivo abierto
                for i in archivo:
                    # Por cada iteraccion que tenga la variable i se pone la palabra reservada end=""
                    # Para que se muestre lo que hay en una linea del texto en una forma continua
                    print (i, end = "")
            # Si no existe el archivo se genera una excepcion FileNotFoundError
            except FileNotFoundError:
                print ("No existe ningun archivo con ese nombre")

        archivo4 = input ("Ingrese el nombre del archivo: ")
        leerArchivo (archivo4)

    if opcion == 5:

        def infoPersonal (nomArchivo):
            try:
                # A la variable archivo se le asigna el directorio de un archivo creado 
                archivo = open (f"C:\\Users\\Sebastian\\OneDrive\\Escritorio\\Clone\\pythontriana\\Ejercicios_instructor\\Ejercicios Archivos\\{nomArchivo}", "x")
                # A esa misma variable se le pasa el modo de apertura a con la misma ruta de archivo
                archivo = open (f"C:\\Users\\Sebastian\\OneDrive\\Escritorio\\Clone\\pythontriana\\Ejercicios_instructor\\Ejercicios Archivos\\{nomArchivo}", "a")
                # Se crean varias variables que significaran los datos de la persona y dichos datos se pasan por consola
                nombre = input ("Ingrese su nombre completo: ")
                edad = int(input("Ingrese cuantos años tiene: "))
                print ("""Indique su tipo de sexo:
1. Masculino
2. Femenino
3. Otro""")
                sexo = int(input ("Ingrese el numero que va acorde a su sexo: "))
                if sexo == 1:
                    sexo = "Masculino"
                if sexo == 2:
                    sexo = "Femenino"
                if sexo == 3:
                    sexo = "Otro"
                ciudad = input ("Ingrese la ciudad en la que vive: ")
                # A la variable archivo que fue con la que abrimos el archivo se le pasa el .write() el cual es para enviar texto al archivo 
                # Con el que se esta llamando, en este caso se crea unos titulos y a dichos titulos se les asigna las variables que contienen
                # Dichos datos correspondientes
                archivo.write (f"""DATOS PERSONALES\n
Nombre completo: {nombre}
Edad: {edad}
Sexo: {sexo}
Ciudad: {ciudad}""")
                # Como no se seguira utilizando el archivo se cierra
                archivo.close ()
            except FileExistsError:
                print ("El archivo que intento crear ya existe")
            except ValueError:
                print ("Usted ingreso un dato no numerico")

        archivo5 = input ("Ingrese el nombre del archivo: ")
        infoPersonal (archivo5)

    if opcion == 6:

        try: 
            # Se creo un metodo para contar los caracteres de un archivo
            def contarCaracter (nomArchivo):
                # Se le asigna a la variable archivo la ruta del archivo que se desea leer con el modo de apertura r que nos permite leer el archivo
                archivo = open (f"C:\\Users\\Sebastian\\OneDrive\\Escritorio\\Clone\\pythontriana\\Ejercicios_instructor\\Ejercicios Archivos\\{nomArchivo}", "r")
                # Cont nos servira para contar el numero de caracteres
                cont = 0
                # Se itera el archivo por medio de un for
                for lineas in archivo:
                    # A cada palabra del archivo se le va a iterar dicha palabra por eso el for anidado
                    for letra in lineas:
                        # Se valida si el caracter que se esta iterando es diferente de un espacion en blanco
                        if letra != " ":
                            # Cada que esta validacion sea True el contador se le suma 1
                            cont = cont + 1
                # Ya finalizado la accion se cierra el archivo
                archivo.close ()   
                # Se imprime la cantidad de caracteres que hay en el archivo ingresado
                print (f"En el archivo se encuentran {cont} caracteres")
        # Si el archivo ya existe generara un error FileExistsError, para eso se antepone al error con un except y su mensaje si se genra dicho error
        except FileExistsError:
            print ("EL archivo ya existe") 
        
        archivo6 = input ("Ingrese el nombre del archivo: ")
        contarCaracter (archivo6)

    if opcion == 7:
        print ("\nHASTA PRONTO\n")
        break