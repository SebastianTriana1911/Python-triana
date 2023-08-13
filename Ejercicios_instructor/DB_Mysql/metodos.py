from proyecto import *

def databases ():
    baseD = input("Ingrese el nombre de la base de datos: ")
    consulta = "CREATE DATABASE %s;"
    valor = (baseD,)
    cursor.execute(consulta,valor)
    bd.commit()

# def tablas ():
#     tabla = input ("Ingrese el nombre que desea que tenga la tabla: ")
#     consulta = "CREATE TABLE %s;"
#     valor = (tabla)
#     cursor.execute(consulta,valor)
#     bd.commit()

# def insertar ():
#     primary = int(input("Ingrese su tipo de documento: "))
#     nombre = input("Ingrese su nombre: ")
#     apellido = input("Ingrese su apellido: ")
#     email = input ("Ingrse su correo: ")
#     consulta = "INSERT INTO aprendiz (documento,nombre,apellido,email) VALUES (%s,%s,%s,%s)"
#     valores = (primary, nombre,apellido,email)
#     cursor.execute(consulta,valores)
#     bd.commit()
#     print ("Listo")

# def mostrarDatos ():
#     try:
#         tabla = input ("Ingrese el nombre de la tabla a la que desea ver los datos: ")
#         documento = int(input("Ingrese numero de documento: "))
#         consulta = "SELECT * FROM %s WHERE documento = %s"
#         valor = (tabla,documento )
#         cursor.execute(consulta,valor)
#         bd.commit()
#     except:
#         print ("El nombre de la tabla no existe")
# tablas()
# insertar()
# mostrarDatos()
databases ()