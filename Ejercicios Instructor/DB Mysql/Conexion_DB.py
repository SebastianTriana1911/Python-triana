# Hacer sentencias SQL desde python

# Importar mysql.connector para la coneccion
import mysql.connector

# A la variable bd se le asigna el metodo connector.connet, donde se le
# Asigna el directorio que es localhost en este caso, el usuario que en 
# Este caso es root, el password que en este caso no tiene, y el database
# Que sera la base de datos que vallamos a manejar
bd = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",  
    database = "conexion_db"
)

# A una variable llamado cursor se le asigna la variable bd mas el metodo cursor
cursor = bd.cursor()

