# Cuantos y cuales son primos

import random 
lista = []
def primos (lista):
    lista2 = []
    cont = 0
    contPrimos = 0
    tam = random.randrange (5,15)
    for i in range (tam):
        numero = random.randrange(0,100)
        lista.append(numero)
    print (lista)

    for q in lista:
        cont = 0
        for w in range (1,q + 1):
            if q % w == 0:
                cont = cont + 1
            else:
                continue 
    
        if cont == 2:
            contPrimos = contPrimos + 1
            lista2.append(q)
    return f"La cantidad de numero primos es {contPrimos} y los numeros son: {lista2}"
print (primos(lista))

