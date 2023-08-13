# Hacer un codigo que tenga una lista de tamaño del 10 al 20 generando numeros aleatorios del 0 al 100 y con esos numeros sacar la suma de todos los 
# elementos de la lista, el promedio, el mayor, el menor, la mediana, la moda y la desviacion estandar 
import random 
lista = []
suma = 0
promedio = 0
mayor = 0
menor = 100000
posicion = 0
cont = 0
maximo = 0
result4 = 0

# Arrojar un numero random para el tamaño de la lista
longitud = random.randint(10,20)
print(f"El tamaño de la lista va a ser de {longitud} elementos")

# Hallar la suma de todos los numeros de la lista y hayar su promedio
for i in range (longitud):
    num = random.randrange(100)
    lista.append (num)
    suma = suma + num
promedio = suma // longitud

print (f"Los elementos de la lista son: {lista}")
print (f"La suma de todos los numeros es: {suma}")
print (f"El promedio de la lista es: {promedio}")

# Hallar el numero mayor y el menor de la lista 
for a in lista:
    if a > mayor:
        mayor = a 
    if a < menor:
        menor = a
print (f"El numero mayor de la lista es: {mayor}")
print (f"El numero menor de la lista es: {menor}")

# Ordenar la lista de menor a mayor
for i in range(longitud):
    for j in range(i+1,longitud):
        if lista[i]>lista[j]:
            aux=lista[i]
            lista[i]=lista[j]
            lista[j]=aux
print (f"La lista organizada de menor a mayor quedaria asi: {lista}")

for i in range(longitud):
    for j in range(i+1,longitud):
        if lista[i]<lista[j]:
            aux=lista[i]
            lista[i]=lista[j]
            lista[j]=aux
print (f"La lista organizada de mayor a menor quedaria asi: {lista}")

# Hallar la mediana de la lista 
if longitud % 2 == 0:
    posicion = (longitud - 1) // 2
    posicion2 = (lista [posicion])
    posicion3 = (lista[posicion + 1])
    posicion = posicion2 + posicion3
    posicion = posicion / 2
    print (f"La mediana de la lista es {posicion}")
elif longitud % 2 != 0:
    posicion = (longitud + 1) // 2
    print (f"La mediana de la lista es: {lista[posicion -1]}")

# Hallar la moda de la lista
for num in lista:
    cont = 0
    for num2 in lista:
        if num == num2:
            cont = cont + 1
    if cont > maximo:
        maximo = cont
        moda = num
print (f"La moda de la lista es: {moda}")

# Hallar la desviacion estandar de la lista 
for b in lista :
    result = b 
    result2 = result - promedio
    result3 = result2 ** 2
    result4 = result4 + result3
desviacion = result4 // longitud
desviacion1 = desviacion ** 0.5
print (f"La desviacion estandar de la lista es: {desviacion1}")