# Hallar el factorial de los numeros de una lista y guradarlos en otro lista. Utilice numeros entre 2 y 15 
# para llenar la lista
import random 

lista = []
lisFactorial = []

def factorial (lista):
    lista = []
    lisFactorial = []
    tam = 5
    factorial = 1
    for i in range (tam):
        numero = random.randrange(2,15)
        lista.append(numero)
    print(lista)
    for q in lista:
            factorial = 1
            for e in range (1, q + 1):
                factorial = factorial * e
            lisFactorial.append(factorial)
    return f"Los factoriales de la lista original son: {lisFactorial}"

print (factorial(lisFactorial))
