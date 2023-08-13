#x,y,z=1,2,3
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

# 3,1,7,2
# Ahora asignamos un for con la variable "i" que recorra desde el elemento 1 hasta el ultimo de la lista, con la burbuja
# que vamos hacer a continuacion va sobrepasar el limite de la variable "tam" por eso se le asigna el -1 para que no se
# pase del valor asignado en la variable "tam" y asi no genere un error 
for i in range(tam-1):
    # Asignamos otro for con la variable "j" que recorrera desde el elemento 2 hasta el ultimo de la lista, esto nos
    # permitira que se compara un valor por el que le sigue 
    for j in range(i+1,tam):
        # Ahora asignaremos una funcion if donde nos indique si el valor que esta el la posicion 1 es mayor al valor
        # que se encuenta en la posicion 2
        if lista[i]>lista[j]:
            # Ahora en una linea de codigo haremos el cambio el elementos para asi poder realizar el cambio de el 
            # elemento menor por el elemento mayor, aca en el codigo asignamos a la lista el elemento de la variable 
            # "i" con la lista en elemento de la variable "j" seguido de un igual y asignamos el elemento de la lista
            # que le corresponde a la variable "j" y a la variable "i", esto significa que el elemento de la variable
            # "i" se cambiara con el elemento de la variable "j" y el elemento de la variable "j" se cambiara con el 
            # elemento de la variable "i", como todo este proceso se hace en una sola linea de codigo no es necesario 
            # crear una variable auxiliar que guarde el elemento de la variable "i" o la variable "j"
            lista[i],lista[j]=lista[j],lista[i]
# Imprimiremos los elementos de la variable "lista" y podremos corroborar lo anteriormente dicho 
print(lista)