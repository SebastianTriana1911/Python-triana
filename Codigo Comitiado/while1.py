# num=1
# print(type(num))
# num="sena"
# print(type(num))

# Se declara una variable "num" y a esa variable se le asigna el valor 1 
num=1
# Se declara una variable "cont" y a esa variable se le asigna el valor de 0
cont=0
# Se declara una variable "sum" y a esa variable se le asigna el valor de 0 
sum=0
# Se declara una variable "menor" y a esa variable se le asigna el valor de 1000000 
menor=1000000
# Se declara una variable "mayor" y a esa variable se le asigna el valor de 0
mayor=0 
# Se crea un bucle while con una condicion de "num" osea 1 no es igual a 0 lo cual es verdadero, lo que quiere decir
# que se llevara acabo el bucle hasta que le asignen un numero que sea 0 a la variable "num"
while num!=0:
    # A la variable "num" se le asigna el numero que ingrese el usuario por consola y el bucle hara que ingrese tantos 
    # como pueda hasta que el numero que ingrese sea 0 para que finalice el bucle
    num=int(input('ingrese numero'))
    # A la variable "cont" que tiene el valor de 0 se le asigna el valor de la variable "cont" + 1, esto hira incrementando
    # segun la cantidad de numeros que ingrese el usuario
    cont=cont+1
    # A la variable "sum" que tiene el valor de 0 se le asigna el valor de la variable "sum" mas la variable "num", esto 
    # quiere decir que a la variable "sum" se le va asignar la suma primer del valor que tenga la variable "sum" (si el 
    # usuario ingresa el numero 1, a la variable "sum" que es 0 en ese momento se le va asignar la suma de 0 que 
    # vale "sum" mas 1 que fue el numero que ingreso el usuario en la variable "num" ahora si el usuario ingresa 
    # el numero 2, a la variable "sum" se le asignara la suma de "sum" que ahora vale 1 mas la variable "num" que ahora
    # vale dos)  y asi quedara guardada la suma de todos los numeros hasta que el usuario ingrese el 0 
    sum=sum+num
    # Ahora se crea una fincion if con una condicion que si la variable "num" es mayor a la variable "mayor" haga, esta 
    # funcion siempre se ejecutara ya que la variable "mayor" tiene un valor a 0 y el usuario no puede insertar un valor
    # menor a 0 ya que si eso pasa no entraria al bucle
    if num>mayor:
        # Como la condicion de la funcion if se va a dar entonces se le esta asignando a la variable "mayor" el numero
        # que sea mas grande entre todos los valores que tiene la variable "num"
        mayor=num
    # Ahora se crea otra otra funcion if donde la condicion es que el valor de la variable "num" sea menor al valor de
    # la variable "menor" esto siempre va a suceder siempre y cuando el usuario no vaya a ingresar un numero mas grande
    # que el valor de la variable "menor" que es 1000000, si dejamos esa condicion hasta ahi el programa nos mostrara 
    # como resultado el numero 0 como el numero menor, y como no queremos eso le vamos a colocar a la funcion if que
    # cumpla la condicion "num" menor a "menor" y el valor de la variable "num" no sea igual a 0
    if num<menor and num!=0:
        # Si la condicion de la funcion if se da entonces se le esta asignando a la variable "menor" el numero
        # que sea menor entre todos los valores que tiene la variable "num" excepto el 0
        menor=num
# Se asigna un print que muestre por consola el valor de la variable "cont" y se le resta uno, esto quiere decir que
# se le va a restar el ultimo valor que se ingrese ya que el ultimo valor va a ser 0 que va hacer el numero clave 
# para acabar con el bucle entonces no es necesario mostrar como si el 0 contara en esa lista
print(f'fueron ingresados {cont-1} numeros')
# Se asigna un print que muestre por consola la suma de todos los numeros 
print(f'La suma es {sum}')
# Se asigna un print que muestre por consola el promedio del valor que tenga la variable "sum" divididolo entre el valor
# que tenga la variable "cont" como podemos ver la variable "cont" esta encerrada entre parentesis junto a un - 1 esto
# quiere decir que la a variable contador se le va a restar el 0 que es el ultimo numero que va a ingresar el usuario
# para terminar el bucle 
print(f'El promedio es {sum/(cont-1)}')
# Se asigna un print que muestre por consola el valor de la variable "mayor" 
print(f'El mayor es {mayor}')
# Se asigna un print que muestre por consola el valor de la variable "menor"
print(f'El menor es {menor}')