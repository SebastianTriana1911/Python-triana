# Añadir a una tupla valores de 0 a 100 en un tamaño de 5 a 15
import random

tupla = ()
tupla1 = ()
tupla2 = ()
longitud = random.randrange (5,15)

for i in range (longitud):
    numeros = random.randrange (1,100)
    tupla = tupla + (numeros, )
print(tupla)