import mysql.connector

bd = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "proyecto"
)

cursor = bd.cursor()