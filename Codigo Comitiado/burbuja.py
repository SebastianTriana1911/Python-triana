# Importamos la funcion random para incorporar elementos de numeros aleatorios a una lista mas adelante 
import random
# Creamos una lista vacia para añadirle elementos con la funcion random
lista=[]
# Esta lista no sera importante en este codigo
cuadrado=[]
# A una variable llamada "tam" que sera la que identifique la longitud de la lista le asignaremos un valor random
# con la funcion random y el metodo randint, pero la longitud de la lista debera de ser entre 5 a 10 elementos 
tam=random.randint(5,10)
# Imprimiremos la variable tam y el resultado es un numero alatorio del 5 al 10 que nos indicara la longitud de la 
# lista 
print(tam)
# Hacemos un for donde nos indique que la variable "i" va a recorrer hasta que llegue a el numero que se le asigno a
# la variable "tam" 
for i in range(tam):
    # Creamos una variable "num" que se le va asignar un numero aleatorio desde el 0 al 100
    num=random.randrange(100)
    # A la variable "lista" le asignaremos como ultimo elemento el valor que contenga la variable "num" y esto se hara
    # hasta que se complete el tamaño de la lista que es el valor que tiene la variable "tam"
    lista.append(num)
# Imprimiremos la lista y veremos como contiene numeros aleatorios hasta el valor que se le declaro a la variable "tam"
print(lista)
# Ahora asignamos un for con la variable "i" que recorra desde el elemento 1 hasta el ultimo de la lista
for i in range(tam):
    # Asignamos otro for con la variable "j" que recorrera desde el elemento 2 hasta el ultimo de la lista, esto nos
    # permitira que se compara un valor por el que le sigue 
    for j in range(i+1,tam):
        # Ahora asignaremos una funcion if donde nos indique si el valor que esta el la posicion 1 es mayor al valor
        # que se encuenta en la posicion 2
        if lista[i]>lista[j]:
            # A una variable "aux" asignele el valor que se encuenta en la posicion 1, esto con la finalidad que a la 
            # hora de hacer el cambio de un valor con otro no se pierda el valor inicial
            aux=lista[i]
            # Ahora como el valor de la posicion 2 es menor al de la posicion 1 , le asignaremos a i el valor de j, ahora
            # "i" y "j" valen lo mismo, por eso colocamos el valor de "i" en una variable auxiliar
            lista[i]=lista[j]
            # Para que a "j" se le asigne el valor inicial que contenia "i", y ahora "i" sera menor que "j", lo que 
            # permitira que la lista quede en un orden de menor a mayor
            lista[j]=aux
# Imprimiremos la lista y veremos como esta ordenado de menor a menor 
print(lista) 
# Toda esta linea de codigo explica lo mismo de lo que se explico anteriormente, lo unico que cambia es el signo de 
# de la linea 46 que cambia de ser mayor a ser menor, lo que significa que la lista tendra un orden de mayor a menor
for i in range(tam):
    for j in range(i+1,tam):
        if lista[i]<lista[j]:
            aux=lista[i]
            lista[i]=lista[j]
            lista[j]=aux
# Imprimiremos los elementos de la variable "lista" y podremos corroborar lo anteriormente dicho 
print(lista)