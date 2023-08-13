# Solicite dos numeros al usuario. Evalua si es factor uno del otro en cualquier orden. Si no son, pida nuevamente dos numeros.
cont = 1

while True:

    print(f"Intento numero {cont}")
    num1 = int(input("Ingrese un numero: "))
    num2 = int(input("Ingrese un numero: ")) 
    cont = cont + 1
    
    if num1 % num2 == 0:
        print (f"El {num1} es factor de {num2}")
        break

    elif num2 % num1 == 0:
        print (f"El {num1} es factor de {num2}")
        break
    