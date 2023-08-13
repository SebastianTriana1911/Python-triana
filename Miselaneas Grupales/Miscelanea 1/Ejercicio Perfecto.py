# Determine si un numero es o no es perfecto . 
# Un numero es perfecto si la suma de sus divisores sin incluir el propio numero es igual a este 

# Se solicita por pantalla un numero
num = int(input("Ingrese un numero: "))
# Se inicializan dos variables result y perfect en 0
result = 0 
perfect = 0

# Se utiliza un bucle for que recorre desde el 1 hasta el numero ingresado
for i in range (1,num):
    # Se le asigna a la variable resultado el resultado del numero ingresado 
    # Por el modulo numero en el que este la variable que lleva la iteracion
    result = num % i
    
    # Se valida si el valor de la variable resultado es igual a 0 si es el caso
    # A la variable perfect se le suma 1 hasta que se acabe la iteracion
    if result == 0:
        perfect = perfect + i
        
# Se valida si el valor de la variable perfect es igual al numero ingresado por pantalla, si es
# igual es perfecto de lo contrario no
if perfect == num:
    print (f"El numero {num} es perfecto")
    
else:
    print (f"El numero {num} no es perfecto")