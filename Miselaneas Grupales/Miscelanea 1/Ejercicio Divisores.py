# Determinar los divisores de un numero introducido por el teclado
# Para determinar si un numero es divisor de un numero el cociente de la divicion tiene que dar 0

# Se solicita por pantalla un numero
num1 = int(input("Ingrese un numero: "))
# Se inicializa la variable resultado en 0
result = 0

# Se itera por un bucle for el numero 1 hastael numero ingresado por el usuario
for i in range (1,num1):
    # A la variable resultado se le asigna el resultado del numero ingresado por el modulo de la 
    # Variable que esta llevando la iteracion que es la variable i
    result = num1 % i

    # Se valida si el valor de la variable resultado es igual a 0, si es el caso la variable de la
    # Iteracion es divisor del numero ingresado por pantalla, si esto no es correcto es por que no 
    # Es divisor
    if result == 0:
        print(f"El numero {i} es divisor de {num1}")

    else: 
        print(f"El numero {i} no es divisor de {num1}")
