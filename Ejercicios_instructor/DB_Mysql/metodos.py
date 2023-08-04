from proyecto import *
def insertar ():
    primary = int(input("Ingrese su tipo de documento: "))
    nombre = input("Ingrese su nombre: ")
    apellido = input("Ingrese su apellido: ")
    email = input ("Ingrse su correo: ")
    consulta = "INSERT INTO aprendiz (documento,nombre,apellido,email) VALUES (%s,%s,%s,%s)"
    valores = (primary, nombre,apellido,email)
    cursor.execute(consulta,valores)
    bd.commit()
    print ("Listo")

def mostrarDatos ():
    try:
        tabla = input ("Ingrese el nombre de la tabla a la que desea ver los datos: ")
        documento = int(input("Ingrese numero de documento: "))
        consulta = "SELECT * FROM %s WHERE documento = %s"
        valor = (tabla,documento )
        cursor.execute(consulta,valor)
        bd.commit()
    except:
        print ("El nombre de la tabla no existe")
mostrarDatos()
# insertar()