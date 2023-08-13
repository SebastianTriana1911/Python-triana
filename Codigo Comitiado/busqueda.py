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
# Asignaremos a una variable "dato" el valor de 5, esto nos permitira saber el numero que queremos buscar 
dato=5
# Creamos un bucle for con la variable "i" que recorra de 1 hasta el numero de elementos que se le asigno a la variable
# "lista"
for i in range(len(lista)):
    # Creamos una funcion if donde nos indique si el valor de la variable "dato" que es 5 es igual a algun elemento de 
    # la lista diga su posicion, como sabemos i recorre cada posicion de la lista y compara si hay algun elemento de la
    # lista que sea igual a 5
    if dato == lista[i]:
        # Si la funcion se cumple mostara cual es el numero que encontro, que seria el 5, y se escribiria asi lista[i],
        # y la posicion se escribiria asi "i" que como sabemos es la variable que recorre cada elemento y esta es la que
        # nos indicara en que posicion es en la que se encuentra 
        print(f'{lista[i]} esta en la posicion {i}')
    # else:
    #     print(f'no esta en la posicion {i}')
