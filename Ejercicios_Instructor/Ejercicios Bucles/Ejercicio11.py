# Determinar los divisores de un numero introducido por el teclado

num1 = int(input("Ingrese un numero: "))
result = 0

for i in range (1,num1):
    result = num1 % i

    if result == 0:
        print(f"El numero {i} es divisor de {num1}")

    else: 
        print(f"El numero {i} no es divisor de {num1}")
