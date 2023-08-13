# For: Solicite al usuario inicio , fin y cantidad a incrementar o decrementar segun el caso. Imprima la serie

ini = int(input("Ingrese el numero por el cual quiere que inicie el contador: "))
fin = int(input("Ingrese el numero el cual determine el fin del contador: "))
increment = int(input("Ingrese el numero el cual determine la cantidad de numeros que se quieren aumentar: "))
cont = 0

while ini > fin:
    ini = int(input("Ingrese el numero por el cual quiere que inicie el contador: "))
    fin = int(input("Ingrese el numero el cual determine el fin del contador: "))
    increment = int(input("Ingrese el numero el cual determine la cantidad de numeros que se quieren aumentar: "))
    
for i in range (ini,fin,increment):
    cont = cont + 1
    print (f"La serie es: {cont}")
    print (f"{i}")

