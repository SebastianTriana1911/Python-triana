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

#in - not in

# for i in range(tam):
#     print(lista[i])

# for dato in lista:
#     print()

# Creamos una funcion donde la condicion es que si 10 no esta dentro de los valores que tiene la variables "lista"
if 10 not in lista:
    # Imprima que si esta 
    print('si esta')
else:  
    # De lo contrado imprima que no esta
    print('no esta')

# Los operadores in y not in, nos sirve para preguntar si algo esta o no esta, como pudimos ver en el ejemplo anterior
# si 10 no estaba, que seria el not in (no esta) imprima una cosa y si si estaba imprimiera otra cosa, lo mismo para 
# con el operador in (si esta) si 10 si estaba tenia que imprimir una cosa de lo contrario debia imprimir otra 