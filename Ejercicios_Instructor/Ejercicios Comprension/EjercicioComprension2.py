# Llenar una lista con numeros aleatorios (reales con un decimal) y que representen calificaciones de un curso, se evaluan de 0 a 5.
# El curso puede tener entre 20 y 30 aprendices. 
# HALLAR
# 1. Genere listas nuevas para los aprobados y los reprobados (se aprueba con 3)
# 2. Genere listas nuevas por cada unidad. Es decir, los que sacan de 0 a 1 son un grupo, los de 1 a 2 otro grupo y asi sucesivamente 
# 3. Diga cual es el promedio de los que aprueban y los que reprueban por separados

# Importar funcion random
import random
# Asignar numeros aleatorios del 20 al 30 a una variable "aprendices"
aprendices = random.randint(20,30)
print (aprendices)
# Asignar numeros reales del 0 al 5 y redondearlos con 1 decimal a una variable "lista" y que se valla llenando desde
# 0 hasta el valor que tenga la variable "aprendices"
lista = [round (random.random () * 5,1 ) for i in range (aprendices)]
print (lista)

# Realizar un ordenamiento burbuja 
for q in range (aprendices):
    for w in range (q+1,aprendices):
        if lista[q] > lista[w]:
            aux = lista[q]
            lista[q] = lista[w]
            lista[w] = aux
print (lista)
# Hacer una comprencion de listas con un if y un else 
lista2 = ["Aprobo" if x >= 3.0 else "Reprobo" for x in lista ]
print (lista2)

# Hallar la posicion elemento que tenga como valor 1.0 o el anterior a este   
posicion1 = 1.0
for i in range (len(lista)):
    if posicion1 < lista[i]:
        print(f"El primer grupo se encuentra desde la posicion 0 hasta la posicion {i - 1}")
        break
# Hallar la posicion elemento que tenga como valor 2.0 o el anterior a este   
posicion2 = 2.0
for e in range (len(lista)):
    if posicion2 < lista[e]:
        print(f"El segundo grupo se encuentra desde la posicion {i} hasta la posicion {e - 1}")
        break
# Hallar la posicion elemento que tenga como valor 3.0 o el anterior a este   
posicion3 = 3.0
for r in range (len(lista)):
    if posicion3 < lista[r]:
        print(f"El tercer grupo se encuentra desde la posicion {e} hasta la posicion {r - 1}")
        break
# Hallar la posicion elemento que tenga como valor 4.0 o el anterior a este
posicion4 = 4.0
for t in range (len(lista)):
    if posicion4 < lista[t]:
        print(f"El cuarto grupo se encuentra desde la posicion {r} hasta la posicion {t - 1}")
        break

# Realizar una rebanada para llenar una lista desde el elemento 0 hasta el valor que tenga la variable "i"
grupo1 = [lista[0:i]]
print (f"Grupo 1 {grupo1}")
# Realizar una rebanada para llenar una lista desde el valor de la variable "i" hasta el valor que tenga la variable "e" 
grupo2 = [lista[i:e]]
print (f"Grupo 2 {grupo2}")
# Realizar una rebanada para llenar una lista desde el valor de la variable "e" hasta el valor que tenga la variable "r"
grupo3 = [lista[e:r]]
print (f"Grupo 3 {grupo3}")
# Realizar una rebanada para llenar una lista desde el valor de la variable "r" hasta el valor que tenga la variable "t"
grupo4 = [lista[r:t]]
print (f"Grupo 4 {grupo4}")
# Realizar una rebanada para llenar una lista desde el valor de la variable "t" hasta el final de la lista, por eso en la
# rebanada, despues de los dos puntos no vemos ningun argumento por que esto nos indica hasta que se terminen los valores 
# de la variable "lista"
grupo5 = [lista[t:]]
print (f"Grupo 5 {grupo5}")

# Hacer la suma de los valores que tenga la lista desde el elemento 0 hasta el valor que le corresponda a la variable "r"
suma1 = 0
for o in lista:
    if o < lista[r]:
        suma1 = suma1 + o
print (f"La suma de todas las calificaciones de los estudiantes que reprobaron es: {round ((suma1), 1)}")
# Hacer la suma de los valores que tenga la lista desde el elemento de la variable "r" hasta el valor que el fin de los 
# valores que tiene la lista
suma2 = 0
for z in lista:
    if z > lista[r - 1]:
        suma2 = suma2 + z
print (f"La suma de todas las calificaciones de los estudiantes que aprobaron es: {round ((suma2), 1)}")

# Hallar la cantidad de elementos que tiene la lista desde 0 hasta el valor de la variable "r"
cont1 = 0
for p in lista:
    if p < lista[r]:
        cont1 = cont1 + 1
print (f"La suma de los elementos de los estudiantes que reprobaron es: {cont1}")
# Hallar la cantidad de elementos que tiene la lista desde el valor de la variable "r" hasta el ultimo valor de la
# lista
cont2 = 0
for c in lista:
    if c > lista[r - 1]:
        cont2 = cont2 + 1
print (f"La suma de los elementos de los estudiantes que aprobaron es: {cont2}")

# Hallar el promedio de todos los estudiantes que reprobaron 
promedio_reprueba = suma1 / cont1
promedio_reprueba = round(promedio_reprueba, 2)
print(f"El promedio de todos los aprendices que reprobaron fue: {promedio_reprueba}")
# Hallar el promedio de todos los estudiantes que aprobaron
promedio_aprueba = suma2 / cont2
promedio_aprueba = round(promedio_aprueba, 2)
print(f"El promedio de todos los aprendices que aprobaron fue: {promedio_aprueba}")
