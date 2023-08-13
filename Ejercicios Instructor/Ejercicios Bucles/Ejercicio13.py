# Determine si un numero es o no es perfecto . Un numero es perfecto si la suma de sus divisores sin incluir el propio 
# numero es igual a este 

num = int(input("Ingrese un numero: "))
result = 0 
cont = 0
perfect = 0

for i in range (1,num):
    result = num % i
    
    if result == 0:
        cont = cont + 1
        
        perfect = perfect + i
        
if perfect == num:
    print (f"El numero {num} es perfecto")
    
else:
    print (f"El numero {num} no es perfecto")