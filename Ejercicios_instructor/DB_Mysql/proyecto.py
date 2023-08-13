import mysql.connector

bd = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = ""
)

cursor = bd.cursor()