# Para que podamos hacer que el sistema nos arroje un numero random desde un numero preedefinido hasta otro numero
# preedefinido, debemos importar la funcion que se llama random esto nos permitira que todos los metodos incorporados
# en esta funcion, se puedan utilizar
import random
# Existe un metodo para hacer que el sistema nos arroje un numero random y es asignandole a una variable un tipo de
# dato entero, ya que el metodo que utilizaremos sera "random" y este metodo por lo general nos dara valores reales
# siguiendo con el proceso, entre corchetes asignando la funcion random y el metodo random, que es el metodo 
# necesario para esta condicion. Seguido de otro parentesis que este nos indicara el rango minimo para que nos arroje
# un numero, segido del argumento "*" mas un numero que nos inticara el rango maximo, cabe aclarar que para asignar 
# el rango maximo el numero que identificara este rango debera estar seguido del argumento "*"
num=int(random.random()*10)
# Imprimiremos por consola la variable "num" y podremos observar que se le asigno un numero random desde el rango 0 
# hasta el rango 10 
print(num)
# Existe otra forma para solicitar un numero random y es declarando una variable que en este caso va a ser "num1" y 
# va a ser igual a la funcion random mas el metodo randint, este metodo nos obligara a ingresar por medio de parentesis
# el valor inicial y el valor final del rango en que queremos que nos de el numero aleatoreo
num1=random.randint(0,100)
# Imprimiremos el valor de la variable "num1" y podremos ver que nos dara un valor desde 0 a 100
print(num1)
# Y la ultima forma que veremos en este ejercicio sera solicitar un numero aleatorio con el metodo randrange, este 
# metodo es casi similar al anterios solo que el anterior era obligatorio colocar el rango de inicio y el rango final
# para buscar el numero aleatorio, pero con el metodo randrange simplemente colocando el ranfo de finalizacion el 
# sistema podra arrojarnos un numero aleatorio sin ningun error
num2=random.randrange(10)
# Imprimiremos ek valor de la variable "num2" y veremos que nos dara un numero entre 0 y 10
print(num2)