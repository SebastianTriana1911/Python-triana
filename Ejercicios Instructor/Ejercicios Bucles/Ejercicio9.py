# Escriba un programa que pregunte cuántos números se van a introducir, pida esos números, y muestre un mensaje 
# cada vez que un número no sea mayor que el primero.

pregunta = int(input("Introduzca la cantidad de numeros que va a ingresar: "))

if pregunta <= 1:
        print("Tiene que ingresar un valor mayor o igual a 1")

else:
    num = int(input("Escriba un número: "))
    
    for i in range(pregunta - 1):
            num2 = int(input(f"Escriba un número más grande que {num}: "))
            if num2 <= num:
                print(f"¡{num2} no es mayor que {num}!")
    
    print("¡Adios!")

