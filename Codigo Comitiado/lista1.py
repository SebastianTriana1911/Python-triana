# CORCHETES [], LLAVES {}, PARENTESIS (), PARENTESIS DENTRO DE LLAVES {()}
# Se esta asignando a la variable "x" el valor 100
x=100
# Se desea ver no el valor de x si no el tipo de dato y esto se logra llamando a la funcion type, el resultado de 
# este print sera int, lo que significa que el valor que tiene "x" es de tipo int osea entero
print(type(x))
# Ahora se le esta asignando a la variable "x" el texto Soacha, lo que significa que ahora ya no es un entero si 
# no un texto
x='Soacha'
# Volveremos a llamar a la funcion type, para saber ahora que tipo de dato es "x", el resultado que nos arrojara
# este print sera str, lo que significa que el valor que tiene "x" es de tipo string osea es una cadena de texto
print(type(x))
# Ahora veremos lo que son las listas, y las listas es una variable a la cual se le puede asignar mas de un valor
# o en otras palabras mas de un elemento, como se puede observar a la variable "lista" se le han asignado muchos 
# elementos, cabe aclarar que para crear una lista en python se deben agrupar todos los elementos de la lista por 
# medio de unas llaves, siguiendo con la explicacion podremos ver que a la lista le asignaron elementos con 
# diferentes tipos de dato, hay str, int y una sublista. Esto significa que la lista es heterogenea osea que 
# contiene muchos tipos de datos. Una cosa muy importante es como llamar a cada elemento de la lista, esto lo 
# veremos mas adelante pero por ahora debemos saber como se enumeran los elementos de las listas, toda lista comienza
# con algo llamado la indexacion en 0, lo que significa que el primer elemento se comienza a contar desde 0 y asi 
# sucesivamente, por ejemplo si queremos llamar al elemento "python" se debera llamar por el 0 
lista=['python',100,[1,2,3,[]],'a']
# Ahora llamaremos nuevamente a la funcion type para que nos muestre que tipo de datos tiene la variable "lista"
# el resultado de este print sera "list", ¿Por que? list es un tipo de dato en python y significa que la variable
# contiene una lista
print(type(lista))
# Llamaremos a la funcion len, esta funcion nos permite saber la longitud que contiene una lista, y en el codigo
# podremos ver como llamamos a la funcion len para que nos diga la longitud que tiene la variable "lista", el 
# resultado sera 4, ya que como podemos ver en la linea 22 hay 4 elementos esta python, 100, [1,2,3,[]] y a
print(len(lista))
# Ahora llamaremos un elemento en particular de la variable lista, como ya sabemos que que toda lista comienza con
# una indexacion en 0, el codigo nos esta diciendo que nos muestre el elemento 0 de la variable "lista". El resultado
# sera python ya que este es el primer elemento que se encuenta en la variable "lista" y  por ende es el numero 0
print(lista[0])
# LLamaremos ahora otro elemento y esta vez sera el 1 que en este caso el resultado sera 100
print(lista[1])
# llamareos ahora otro elemento y esta vez sera el 3 que en este caso el resultado sera a. Para la variable "lista"
# ya no hay mas elementos lo que significa que si queremos buscar el elemento 4, nos saldra error ya que no podra
# buscar un elemento que no existe
print(lista[3])
# Ahora llamaremos el elemento -4, para entender esto debemos saber que cuando llamamos un elemento en una manera 
# negativa lo llamaremos de atras para adelante, lo que significa que el primer valor sera el ultimo y asi de 
# adelante para atras y su indexacion empezara en -1, por ejemplo el elemento -1 sera el a y en este caso el elemento
# -4 sera python
print(lista[-4])
# La funcion del nos sirve para eliminar el elementos de una lista que nosotros deseemos, como podemos ver estamos 
# llamando a la funcion del, seguido de la variable "lista" que es la variable que contiende la lista con los 
# elementos que queremos eliminar, seguido de dos corchetes que adentro contienen el numero que nos indica la 
# posicion del elemento que deseamos eliminar, en este caso deseamos eliminar el elemento -2, segun lo anteriormente
# explicado el valor -2 sera [1,2,3,[]]
del lista[-2]
# Ahora la lista cambiara y estamos diciendo que muestre el contenido de la variable "lista" la cual ahora se tendria
# que ver asi: ['python', 100, 'a']
print(lista)
# Estos fragmentos de codigo nos dan la explicacion de que toda variable es una clase y que los metodos que esta
# en los diagramas de clases aca son los mismos metodos con la misma sintaxis, esto quiere decir que el metodo 
# depende de un objeto o clase para que esta exista y está, es conectada por medio del argumento "."
"""
cuenta1=cuenta()
cuenta2=cuenta()
cuenta3=cuenta()
cuenta1.deposit()
print(type(cuenta1))
cuenta2.deposit()
cuenta3.deposit()
"""