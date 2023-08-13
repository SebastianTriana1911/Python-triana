# Llenar un arreglo de n elementos con numeros generados con la fncion random. N es ingresado por el usuario. Disene un menu con las siguientes 
# operaciones

import random


# Agregar numeros aleatorios a una lista con una longitud aleatoria
def num_random (tam,numero):
    lista = []
    tam = random.randrange (10,20)
    lista = [random.randrange (numero) for w in range (tam)]
    return lista 
lista2 = num_random(15,30)
print (lista2)

# Hacer una suma con todos los elementos de la lista
def suma_lista (lista):
    suma = 0
    for q in lista:
        suma = suma + q
    return suma
print(f"La suma de todos los elementos es: {suma_lista(lista2)}")

# Hallar el promedio de la lista
def promedio_lista (lista):
    return suma_lista(lista) / len(lista)
print(f"El promedio de la lista es: {promedio_lista(lista2)}")

# Hallar el numero mayor de toda la lista
def mayor_lista (lista):
    mayor = 0
    for e in lista:
        if e > mayor:
            mayor = e
    return mayor
print (f"El numero mayor de la lista es: {mayor_lista(lista2)}")

# Hallar el numero menor de toda la lista 
def menor_lista (lista):
    menor = 10000
    for r in lista:
        if r < menor:
            menor = r
    return menor
print (f"El numero menor de la lista es: {menor_lista(lista2)}")

# Organizar la lista de mayor a menor 
def desendente (lista):
    for t in range (len(lista)):
        for y in range (t+1, len(lista)):
            if lista[t] < lista[y]:
                aux = lista[y]
                lista[y] = lista[t]
                lista[t] = aux
    return lista
print (f"La lista de mayor a menor: {desendente(lista2)}")

# Organizar la lista de menor a mayor 
def asendente (lista):
    for t in range (len(lista)):
        for y in range (t+1, len(lista)):
            if lista[t] > lista[y]:
                aux = lista[y]
                lista[y] = lista[t]
                lista[t] = aux
    return lista
print (f"La lista de menor a mayor: {asendente(lista2)}")

# Hallar la moda de la lista
def moda_lista (lista):
    maximo = 0
    moda = 0
    for num1 in lista:
        cont = 0
        for num2 in lista:
            if num1 == num2:
                cont = cont + 1
        if cont > maximo:
            maximo = cont
            moda = num1
    if cont == maximo:
        return "no hay moda"
    return f"La moda de la lista es: {moda}"
print(moda_lista(lista2))

# Hallar la mediana en la lista
def mediana_lista (lista):
    if len(lista) % 2 == 0:
        posicion = (len(lista) - 1) // 2    
        posicion2 = (lista [posicion])
        posicion3 = (lista [posicion + 1])
        posicion = posicion2 + posicion3
        posicion = posicion / 2
    elif len(lista) % 2 != 0:
        posicion = (len(lista) + 1) // 2
        return f"La mediana de la lista es: {lista [posicion -1]}"
    return f"La mediana de la lista es {posicion}"
print (mediana_lista(lista2))

# Buscar si se encuentra el número en la lista 
numero1 = int(input("Ingrese un numero: "))
def buscar_lista (lista):
    while True:
        if numero1 in lista:
            break
        else:
            return f"El numero {numero1} no esta"
    return f"El numero {numero1} si esta"
print (buscar_lista(lista2))

# Buscar en qué posición está el numero que ingreso
def posicion_lista (lista2):
    posicion = []
    for i in range (len(lista2)):
        if numero1 == lista2[i]:
            posicion.append (i)
    return f"El numero se encuentra en la posicion {posicion}"
print (posicion_lista(lista2))

# Buscar cuantas veces esta el numero que ingreso
def veces_lista (lista2):
    cantidad = []
    cont = 0 
    for y in range (len(lista2)):
        if numero1 == lista2[y]:
            cont = cont + 1
        cantidad = cont
    return f"Las veces que se encontro el numero {numero1} fue: {cantidad}"
print(veces_lista(lista2))
