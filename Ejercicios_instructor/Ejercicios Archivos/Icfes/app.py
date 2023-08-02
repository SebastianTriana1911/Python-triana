from persona import *
import csv

with open ("C:\\Triana\\Saber_11.csv") as archivo:
    saber = csv.reader (archivo)
    for i in saber:
        persona = Persona (i[])