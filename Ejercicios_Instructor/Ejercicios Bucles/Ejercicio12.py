# Determinar si un numero es primo o no 

num = int(input("Ingrese un numero: "))
result = 0 
cont = 0

for i in range (1,num):
    result = num % i
    
    if result == 0:
        cont = cont + 1

if cont >= 3:
    print (f"El numero {num} no es primo")
    
else:
    print (f"El numero {num} es primo")