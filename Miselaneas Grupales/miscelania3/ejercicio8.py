# Suma pares y promedio de los impares
import random
lista = []
def suma_pares (lista):
    sumpar = 0
    tam = random.randrange (5,15)
    for i in range (tam):
        numero = random.randrange (0,100)
        lista.append(numero)
    for a in lista:
        if a % 2 == 0:
            sumpar = sumpar + a
    return f"La lista es {lista}\nY la suma de todos los pares es: {sumpar}"
print (suma_pares(lista)) 

def promedio_impar (lista):
    sumimpar = 0
    cont = 0
    for a in lista:
        if a % 2 != 0:
            cont = cont + 1
            sumimpar = sumimpar + a
    promedio = sumimpar / cont
    return f"La lista es {lista}\nY el promedio de todos los impares es: {promedio}"
print (promedio_impar(lista))


