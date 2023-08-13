# Llenar una lista por comprension basada en otra lista previamente llena ( por comprension aleatoriamente) con numeros. Si el dato es par llene
# llene la lista con la raiz del numero pero si es impar llenelo con el numero elevado al cuadrado

import random 
import math 

tam = random.randint (5,10)
lista = [random.randrange(100) for i in range (tam)]
print (lista)
lista2 = [math.sqrt(x) if x % 2 == 0 else x ** 2 for x in lista]
print (lista2)