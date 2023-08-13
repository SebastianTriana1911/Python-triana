# Crearemos una lista la cual no contenga elementos lo que quiere decir que va a ser una lista vacia
lista=[]
# A la variable "lista" le vamos a agregar el valor 100 con el metodo append
lista.append(100)
# A la variable "lista" ahora le vamos a agregar el valor 50 con el metodo append, recordemos que este metodo se 
# utiliza para insertar un elemento en la ultima posicion de una lista, como ya agregamos el valor 100 a la lista
# ahora el 50 hira despues del 100, lo que significa que la lista se veria asi: [100, 50] y su sintaxis es una 
# variable conectada por un punto seguida del metodo que en este caso es append y entre parentecis el valor que se 
# desea añadir a la ultima posicion de la lista
lista.append(50)
# A la variable "lista" ahora le vamos a agregar el valor -100 con el metodo append
lista.append(-100)
# A la variable "lista" ahora le vamos a agregar el valor 20 con el metodo append
lista.append(20)
# A la variable "lista" ahora le vamos a agregar el valor 5 con el metodo append
lista.append(5)
# Imprimiremos la valiable "lista" y veremos que contendra todos los valores que previamente le ingresamos lo que 
# hara que la lista se vea asi: [100, 50, -100, 20, 5]
print(lista)
# Ahora le vamos a agregar a la variable "lista" un nuevo elemento pero ahora con el metodo insert, el metodo insert
# consiste en añadir un nuevo elemento a una lista pero a diferencia del append que lo envia a la ultima posicion de 
# la lista, insert nos permitira agregar dicho elemento en la posicion que deseemos, cabe recalcar que no se eliminara
# ningun elemento si no se correran, su sintaxis es una variable conectado por el argumento "." seguido del metodo 
# insert y entre parentecis se colocara el numero de la posicion que deseamos que esté el elemento que queremos
# añadir, separado por el argumento "," seguido del elemento que deseamos insertar, en el ejemplo podemos ver que 
# se desea insertar el string "prueba" en la posicion menos dos, como sabemos, cuando el numero de la posicion es 
# negativo se contara de derecha a izquienda con una indexacion de -1 esto quiere decir que el primer elemento estara
# en la posicion -1 el siguiente en la -2 y asi sucesivamente
lista.insert(-2,'prueba')
# Se desea imprimir la lista nuevamente para que nos muestre el cambio que acabamos de hacer, y el resultado sera este
# [100, 50, -100, 'prueba', 20, 5] 
print(lista)
