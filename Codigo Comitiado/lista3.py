# Importaremos la funcion random para poder hacer que el sistema nos arroje un numero alazar 
import random
# Crearemos una variable llamada "lista" con un tipo de dato list y esta no contendra ningun elemento
lista=[]
# Crearemos una variable llamada "cuadrado" con un tipo de dato list y esta no contendra ningun elemento
cuadrado=[]
# Ahora le vamos a asignar a la variable "tam" el numero random que nos arroje el sistema que en este caso sera un 
# numero del 5 al 10, a la variable "tam" le asignamos el numero que nos arroje la funcion random seguida por el 
# metodo randint, con la condicion que el numero este en el rango de 5 hasta el 10 
tam=random.randint(5,10)
# Imprimiremos la variable "tam" para saber cual es el valor que se le asigno gracias a la funcion random 
print(tam)
# Ahora crearemos un bucle for que nos indicara en donde queremos que empieze el ciclo que en este caso va a ser 1,
# y donde queremos que termine que en este caso sera el valor asignado a la variable "tam"
for i in range(tam):
    # Le asignamos a la variable "num" el valor random que nos arroje el sistema desde 1 hasta el 100
    num=random.randrange(100)
    # Ahora a la variable "lista" le vamos a insertar en la ultima posicion el valor que se le haya asignado a la 
    # variable "num", desde aqui vuelve al inicio y volvera hacer el mismo procedimiento hasta que se cumpla la
    # condicion del for que es que termine en el valor asignado de la variable "tam"
    lista.append(num)
# Una vez finalizado el ciclo imprimiremos la lista que ahora contendra 10 elementos
print(lista)
# Crearemos nuevamente un ciclo for con una variable "i" donde recorra todos los elementos de la variable "lista"
for i in range(len(lista)):
    # A la variable "cuadrado" que ya sabemos que es de tipo de dato list, le asignaremos en la ultima posicion, la
    # operacion del valor que tenga la variable "i" (que el valor seria un elemento de la valiable "lista", dependiendo
    # del recorrido que lleve), elevado al cubo. Entonces el resultado de esa operacion sera el valor que se inserte
    # a la variable "cuadrado". Este ciclo finalizara hasta que i sea el ultimo elemento de la variable "lista"
    cuadrado.append(lista[i]**2)
    #lista[i]=lista[i]**2
    # print(lista[i]*lista[i])
    # print(lista[i]**2)
    # print(math.pow(lista[i],2))
# Imprimiremos los elementos que contenga la variable "cuadrado" que como sabemos es el resultado de todos los 
# elementos de la variable "lista" elevados al cuadrado
print(cuadrado)
print(sum(lista))