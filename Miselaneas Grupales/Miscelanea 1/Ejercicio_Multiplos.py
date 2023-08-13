# Determinar cuales son los múltiplos de 5 comprendidos entre 1 y N.

# Se pide un numero por consola
n = int(input("Ingrese un numero: "))

# Se itera en la variable i el numero 1 hasta el numero ingresado por consola
for i in range (1, n + 1):
    # En una variable multiplo se asigna el valor de la multilicacion de 5 
    # Entre el valor que este iterando la variable i
    multiplo = 5 * i
    # Se muestra en pantalla los multiplos
    print (f"El numero {multiplo} es multiplo de 5")