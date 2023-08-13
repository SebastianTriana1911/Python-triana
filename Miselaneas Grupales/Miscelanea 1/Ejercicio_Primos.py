# Determinar si un numero es primo o no 
# Un numero primo es el numero que tiene dos divisores el 1 y el mismo

# Se solicita por pantalla un numero
num = int(input("Ingrese un numero: "))
# Se inicializan dos variables result y cont en 0
result = 0 
cont = 0

# Se utiliza un bucle for que recorre desde el 1 hasta el numero ingresado
for i in range (1,num + 1 ):
    # Se le asigna a la variable resultado el resultado del numero ingresado 
    # Por el numero en el que este la variable que lleva la iteracion
    result = num % i
    
    # Se valida si el valor de la variable resultado es 0, si es asi a la 
    # Variable const se le suma 1 y se le ira sumando 1 siempre y cuando 
    # Resultado sea 0 y se valide desde el numero 1 hasta el numero ingresado
    if result == 0:
        cont = cont + 1

# Si cont llega a valer 3 o mas de 3 es por que el numero ingresado por el
# Usuario no es primo de lo contrario si lo es
if cont >= 3:
    print (f"El numero {num} no es primo")
    
else:
    print (f"El numero {num} es primo")