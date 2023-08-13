from Conexion_DB import *

# Se crea un metodo que funcione para insertar datos en una tabla
def insertDatos():
    # Se crean variables que correspondan con cada uno de los campos que 
    # Contenga la tabla personas
    primary = int(input("Ingrese su tipo de documento: "))
    nombre = input("Ingrese su nombre: ")
    apellido = input("Ingrese su apellido: ")
    email = input ("Ingrese su correo: ")
    # Se crea la sentencia SQL para la insercion
    consulta = "INSERT INTO personas (documento,nombre,apellido,email) VALUES (%s,%s,%s,%s)"
    # La variable valores remplaza cada uno de los %s por el valor de cada variable
    valores = (primary, nombre, apellido, email)
    # El cursor.execute permite guardar la consulta con los valores ya cambiados a
    # La variable cursor
    cursor.execute(consulta,valores)
    # bd que es la variable que contiene la conexion con el .commit() permite enviar
    # La sentencia SQL a la base de datos para realizar la insercion con exito
    bd.commit()
    print ("Datos ingresados correctamente")


def selectDatos ():
    # Se crea un menu que muestre algunas convinaciones de las consultas select
    print ("""Ingrese lo que desea consultar
           1. Documentos
           2. Nombres
           3. Apellidos
           4. Emails
           5. Todos los datos de una persona
           6. Todos los datos
""")
    # La opcion que escoja el usuario es la variante de la consulta
    opcion = int (input("Ingrese el numero de la opcion que desea realizar: "))
    if opcion == 1:
        # En este caso decidio solo ver los documentos por esa razon se cambia el * por
        # Documentos
        consulta = "SELECT documento FROM personas"
        # Al cursor se le pasa la consulta para luego iterar sobre cursor que es el que
        # Ya cuenta con el resultado de la consulta
        cursor.execute(consulta, )
        # Se itera para que se muestre los documentos de 1 en 1
        for documentos in cursor:
            # Para no mostrar todos los datos en tuplas se asigna la posicion en la que 
            # Estan los documentos, como solo desearemos ver un campo ese campo siempre 
            # Estara en el indice 0
            print (f"""------------------------
{documentos[0]}
------------------------""")
    if opcion == 2:
        consulta = "SELECT nombre FROM personas"
        cursor.execute(consulta, )
        for nombres in cursor:
            print (f"""------------------------
{nombres[0]}
------------------------""")
    if opcion == 3:
        consulta = "SELECT apellido FROM personas"
        cursor.execute(consulta, )
        for apellido in cursor:
            print (f"""------------------------
{apellido[0]}
------------------------""")
    if opcion == 4:
        consulta = "SELECT email FROM personas"
        cursor.execute(consulta, )
        for email in cursor:
            print (f"""------------------------
{email[0]}
------------------------""")
    if opcion == 5:
        documento = int(input("Ingrese el documento de la persona a la que desea verle los datos: "))
        consulta = "SELECT * FROM personas WHERE documento = %s"
        valor = (documento,)
        cursor.execute(consulta, valor)
        for datos in cursor:
            print (f"""------------------------
Documento - {datos[0]}
Nombre - {datos[1]}
Apellidos - {datos[2]}
Email - {datos[3]}
------------------------""")
    if opcion == 6:
        consulta = "SELECT * FROM personas"
        cursor.execute(consulta, )
        for datos in cursor:
            print (f"""------------------------
Documento - {datos[0]}
Nombre - {datos[1]}
Apellidos - {datos[2]}
Email - {datos[3]}
-------------------------
\n""")
    # Si la variable opcion no guarda ninguno de los numeros de las opciones
    # Del menu se le mostrara un mensaje
    if opcion != 1 or 2 or 3 or 4 or 5 or 6:
        print ("Usted escribio un dato erroneo")


def deleteDatos ():
    documento = input ("Ingrese el documento de la persona que desea eliminar: ")
    consulta = "DELETE FROM personas WHERE documento = %s"
    valor = (documento, )
    cursor.execute(consulta, valor)
    bd.commit ()

selectDatos ()
