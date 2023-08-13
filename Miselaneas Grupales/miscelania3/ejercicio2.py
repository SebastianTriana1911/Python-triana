# Llenar dos arreglos de n elementos con números generados con la función random. Compararlos y decir:
import random

lista1 = []
lista2 = []

def llenarLista (lista):
    lista = []
    tam = random.randrange (5,15)
    for i in range (tam):
        numero = int (random.randrange(0,50))
        lista.append(numero)
    return lista

lista1 = llenarLista(lista1)
lista2 = llenarLista(lista2)
print (f"La lista1 es: {lista1}")
print (f"La lista2 es: {lista2}")

# Cuál de los dos tiene la suma más alta
def sumaLista (lista):
    suma = 0
    for i in lista:
        suma = suma + i
    return suma
sumal1 = sumaLista(lista1)
sumal2 = sumaLista(lista2)
print (f"La suma de la lista1 es de: {sumaLista(lista1)}")
print (f"La suma de la lista2 es de: {sumaLista(lista2)}")

def sumaMayor (lista1,lista2):
    if lista1 > lista2:
        return f"La suma mayor es la de la lista1 con la suma de: {lista1}"
    else:
        return f"La suma mayor es la de la lista2 con la suma de: {lista2}"
print (sumaMayor(sumal1,sumal2))


# Cuál de los dos tiene el número mayor
def mayorLista (lista):
    mayor = 0
    for e in lista:
        if e > mayor:
            mayor = e
    return mayor
print (f"El numero mayor de la lista1 es: {mayorLista(lista1)} ")
print (f"El numero mayor de la lista2 es: {mayorLista(lista2)} ")
mayorl1 = mayorLista(lista1)
mayorl2 = mayorLista(lista2)

def maxLista (mayor1,mayor2):
    if mayor1 > mayor2:
        return f"La lista con numero mayor es la lista1 y su numero es: {mayor1}"
    elif mayor1 < mayor2:
        return f"La lista con numero mayor es la lista2 y su numero es: {mayor2}"
    else:
        return f"Las dos listas tienen el mismo numero mayor y es: {mayor1}"
print(maxLista(mayorl1,mayorl2))

# Cuál de los dos tiene el número menor
def menorLista (lista):
    menor = 10000
    for e in lista:
        if e < menor:
            menor = e
    return menor
print (f"El numero menor de la lista1 es: {menorLista(lista1)} ")
print (f"El numero menor de la lista2 es: {menorLista(lista2)} ")
menorl1 = menorLista(lista1)
menorl2 = menorLista(lista2)

def minLista (menor1,menor2):
    if menor1 > menor2:
        return f"La lista con numero menor es la lista2 y su numero es: {menor2}"
    elif menor1 < menor2:
        return f"La lista con numero menor es la lista1 y su numero es: {menor1}"
    else:
        return f"Las dos listas tienen el mismo numero menor y es: {menor1}"
print (minLista(menorl1,menorl2))

# Sacar el promedio de cada uno
def promedio (lista):
    prom = round (sumaLista(lista) / len(lista), 2) 
    return prom
print (f"El promedio de la lista1 es: {promedio(lista1)}")
print (f"El promedio de la lista2 es: {promedio(lista2)}")
proml1 = promedio(lista1)
proml2 = promedio(lista2)

# Sacar el promedio en conjunto y decir si el promedio de la lista1 y el de la lista2 está por encima o por debajo del arreglo conjunto
def promConjunto (l1,l2):
    sumaTotal = sumal1 + sumal2
    tamTotal = len(l1) + len(l2)
    promConj = round (sumaTotal / tamTotal, 2)
    return promConj
print (f"El promedio conjunto entre la lista1 y la lista2 es de: {promConjunto(lista1,lista2)}")
promConj = promConjunto(lista1,lista2)

def comparaProm1 (prom1,prom3):
  if prom1 > prom3:
   return f"El promedio de la lista1 {proml1} esta por encima del promedio en conjunto {promConj}"
  elif prom1 < prom3:
    return f"El promedio de la lista1 {proml1} esta por debajo del promedio en conjunto {promConj}"
  else:
    return f"El promedio de la lista1 {proml1} es igual al promedio en conjunto {promConj}"
print(comparaProm1(proml1,promConj))

def comparaProm2 (prom2,prom4):
   if prom2 > prom4:
    return f"El promedio de la lista2 {proml2} esta por encima del promedio en conjunto {promConj}"
   elif prom2 < prom4:
    return f"El promedio de la lista2 {proml2} esta por debajo del promedio en conjunto {promConj}"
   else:
    return f"El promedio de la lista2 {proml2} es igual al promedio en conjunto {promConj}"
print(comparaProm2(proml2,promConj))

# Cuál de los dos tiene mayor cantidad de pares
def cantidadPar (lista):
    cont = 0
    for i in lista:
        if i % 2 == 0:
            cont = cont + 1
    return cont 
print (f"La cantidad de pares que hay en la lista1 es de {cantidadPar(lista1)}")
print (f"La cantidad de pares que hay en la lista2 es de {cantidadPar(lista2)}")
parl1 = cantidadPar(lista1)
parl2 = cantidadPar(lista2)

def comparaPar (par1,par2):
   if par1 > par2:
      return f"La lista1 tiene mayor cantidad de pares con una cantidad de: {parl1}"
   elif par1 < par2:
      return f"La lista2 tiene mayor cantidad de pares con una cantidad de: {parl2}"
   else:
      return f"Las dos lista tiene la misma cantidad de pares con una cantidad de: {parl2}"
print (comparaPar(parl1,parl2))

# Cuál de los dos tiene mayor cantidad de impares
def cantidadImpar (lista):
    cont = 0
    for i in lista:
        if i % 2 != 0:
            cont = cont + 1
    return cont 
print (f"La cantidad de impares que hay en la lista1 es de {cantidadImpar(lista1)}")
print (f"La cantidad de impares que hay en la lista2 es de {cantidadImpar(lista2)}")
imparl1 = cantidadImpar(lista1)
imparl2 = cantidadImpar(lista2)

def comparaImpar (impar1,impar2):
   if impar1 > impar2:
      return f"La lista1 tiene mayor cantidad de impares con una cantidad de: {imparl1}"
   elif impar1 < impar2:
      return f"La lista2 tiene mayor cantidad de impares con una cantidad de: {imparl2}"
   else:
      return f"Las dos lista tiene la misma cantidad de impares con una cantidad de: {imparl2}"
print (comparaImpar(imparl1,imparl2))
