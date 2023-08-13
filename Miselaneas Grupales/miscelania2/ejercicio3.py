# Importar la funcion random
import random

# Asignar variables
lista1 = []
lista2 = []
suma1 = 0
suma2 = 0
mayor1 = 0
mayor2 = 0
menor1 = 10000
menor2 = 10000
par1 = 0
par2 = 0
impar1 = 0
impar2 = 0

# Asignarle 8 elementos a la lista1 y a la lista2 mediante un for range con numeros aleatorios del 0 al 10 con la 
# funcion random y metodo randint 
for i in range(8):
    num1 = random.randint(0,10)
    lista1.append(num1)
print (lista1)

for n in range(8):
    num2 = random.randint(0,10)
    lista2.append(num2)
print (lista2)

# Sacar el promedio de la lista1 y la lista2 sumando todos los elementos de la lista y dividiendolo en la cantidad 
# de elementos que estos dos arreglos contienen
for s in lista1:
    suma1 = suma1 + s
promedio1 = suma1 / 8
    
for e in lista1:
    suma2 = suma2 + e
promedio2 = suma2 / 8

# Sumar todos los elementos de la lista1 y la lista2 y compararlos entre los dos pa saber que lista contiene la suma
# mayor
if suma1 > suma2:
    print (f"La suma mayor es la de la lista1 y la suma de sus elementos es: {suma1}")
else:
    print (f"La suma mayor es la de la lista2 y la suma de sus elementos es: {suma2}")

# Encontrar cual es el numero mayor y el numero menor de la lista1 
for a in lista1:
    if a > mayor1:
        mayor1 = a
    if a < menor1:
        menor1 = a
print (f"El numero mayor de la lista1 es: {mayor1}")
print (f"El numero menor de la lista1 es: {menor1}")

# Encontrar cual es el numero mayor y el numero menor de la lista2
for b in lista2:
    if b > mayor2:
        mayor2 = b
    if b < menor2:
        menor2 = b
print (f"El numero mayor de la lista2 es: {mayor2}")
print (f"El numero menor de la lista2 es: {menor2}")

# Comparar cual es el numero mayor entre las dos listas
if mayor1 > mayor2:
    print(f"El numero mayor entre las dos listas es: {mayor1}")
elif mayor1 < mayor2:
    print(f"El numero mayor entre las dos listas es: {mayor2}")
else:
    print(f"Ambos numeros son iguales")

# Comparar cual es el numero menor entra las dos listas 
if menor1 > menor2:
    print(f"El numero menor entre las dos listas es: {menor2}")
elif menor1 < menor2:
    print(f"El numero menor entre las dos listas es: {menor1}")
else:
    print(f"Ambos numeros son iguales")

# Como ya se hayo el promedio de la lista1 y la lista2 ahora se sacara el promedio de esas dos listas para que de
# el promedio en conjunto     
print (promedio1, promedio2)
promedio_conj = (promedio1 + promedio2) / 2
print (f"El promedio entre las dos listas es: {promedio_conj}")

# Comparar si el promedio de la lista1 supera, iguala o no sumepera el promedio en conjunto de las dos listas
if promedio1 > promedio_conj:
    print (f"El promedio de la lista1 {promedio1} esta por encima de el promedio en conjunto {promedio_conj}")
elif promedio1 < promedio_conj:
    print (f"El promedio de la lista1 {promedio1} esta por debajo de el promedio en conjunto {promedio_conj}")
else:
    print (f"El promedio de la lista1 {promedio1} es igual al promedio en conjunto {promedio_conj}")

# Comparar si el promedio de la lista2 supera, iguala o no sumepera el promedio en conjunto de las dos listas
if promedio2 > promedio_conj:
    print (f"El promedio de la lista2 {promedio2} esta por encima de el promedio en conjunto {promedio_conj}")
elif promedio2 < promedio_conj:
    print (f"El promedio de la lista2 {promedio2} esta por debajo de el promedio en conjunto {promedio_conj}")
else:
    print (f"El promedio de la lista2 {promedio2} es igual al promedio en conjunto {promedio_conj}")

# Hallar cuantos numeros son pares dentro de la lista1
for lis1 in lista1:
    if lis1 % 2 == 0:
        par1 = par1 + 1
    else:
        continue
print (f"La cantidad de pares que hay en la lista1 es de: {par1}")

# Hallar cuantos numeros son impares dentro de la lista1
for lis1 in lista1:
    if lis1 % 2 != 0:
        impar1 = impar1 + 1
    else:
        continue
print (f"La cantidad de impares que hay en la lista1 es de: {impar1}")

# Hallar cuantos numeros son pares dentro de la lista2
for lis2 in lista2:
    if lis2 % 2 == 0:
        par2 = par2 + 1
    else:
        continue
print (f"La cantidad de pares que hay en la lista2 es de: {par2}")
# Hallar cuantos numeros son impares dentro de la lista2
for lis2 in lista2:
    if lis2 % 2 != 0:
        impar2 = impar2 + 1
    else:
        continue
print (f"La cantidad de impares que hay en la lista2 es de: {impar2}")

# Comparar entre los pares de la lista1 y la lista2 para saber que lista tiene la mayor cantidad de pares
if par1 > par2:
    print (f"La lista1 tiene mayor cantidad de pares con una cantidad de: {par1}")
elif par1 < par2:
    print (f"La lista2 tiene mayor cantidad de pares con una cantidad de: {par2}")
else:
    print (f"Ambas listas tiene la misma cantidad de pares con: {par1} y {par2}")

# Comparar entre los pares de la lista1 y la lista2 para saber que lista tiene la mayor cantidad de impares
if impar1 > impar2:
    print (f"La lista1 tiene mayor cantidad de impares con una cantidad de: {impar1}")
elif impar1 < impar2:
    print (f"La lista2 tiene mayor cantidad de impares con una cantidad de: {impar2}")
else:
    print (f"Ambas listas tiene la misma cantidad de impares con: {impar1} y {impar2}")