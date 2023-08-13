# Hacer un codigo donde el programa escoja un numero aleatorio del 0 al 10 sin que el usuario sepa cual es el numero,
# el usuario ingresara un numero, si este es menor que el numero escogido por el programa, se mostrara un mensaje 
# que el numero es mayor al que puso, y si es mayor pues debera mostrar que el numero es menor al que ingreso, si 
# el numero que ingrese el igual al numero escogido por el programa se le dira felicitaciones. 

from random import randint
incognita = randint (0,100)

while True:
    numero = int(input("Ingrese un numero: "))
    if numero < incognita:
        print (f"El numero incognito es mayor que {numero}")
        continue
    elif numero > incognita:
        print (f"El numero incognito es menor que {numero}")
        continue
    else:
        print(f"Felicidades el numero incognito era: {incognita}")
        break