# Diseñar e implementar un programa que solicite a su usuario un valor no negativo n y visualice 
# la siguiente salida:

# La variable num contendra un numero ingresado por consola
num = int(input("Ingrese un numero: "))

# La variable i iterara por medio de un bucle for desde el numero, hasta 0
for i in range(num,0,-1):
    # La variable a terara desde 1 hasta le valor que contenga la variable i
    for a in range(1,i +1):
        # Cada iteracion que tenga la variable a se imprimira de corrido gracias a la palabra reservada
        # end = ""
        print(a, end=" ")
    # Se imprime un espacion en blanco para que la iteracion que tenga a no siga de largo
    print()