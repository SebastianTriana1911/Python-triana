# Escriba un programa que pida dos números enteros y escriba la suma de todos los enteros desde el primer número
# hasta el segundo.

result = 0
val = int(input("Escriba un numero entero pisitivo: "))

if val <= 0:
    print ("Le e pedido un numero entero positivo")
else: 
    val2 = int(input(f"Escriba un numero entero mayor a {val}: "))
    if val2 <= val:
        print ("Le e pedido un numero mayor")
    else:
        
        for i in range (val,val2 + 1):
            result = result + i
            

    print(f"La suma {val} + {val2} es = {result} ")
    

