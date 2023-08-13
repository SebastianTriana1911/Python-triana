# Escriba un programa que pida dos números enteros y escriba la suma de todos los enteros desde el primer número
# hasta el segundo.

result = 0
val = int(input("Escriba un numero que sea positivo: "))

if val <= 0:
    print ("El numero que ingreso no es positivo")
else: 
    val2 = int(input(f"Escriba un numero que sea mayor a {val}: "))

    if val2 <= val:
        print (f"EL numero que ingreso no es mayor a {val}")
    else:
        
        for i in range (val,val2 + 1):
            result = result + i
            
    print(f"La suma {val} + {val2} es = {result} ")
    

