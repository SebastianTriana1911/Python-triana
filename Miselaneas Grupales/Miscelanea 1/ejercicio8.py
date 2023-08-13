# Determinar cuales son los múltiplos de 5 comprendidos entre 1 y N.

n = int(input("Ingrese un numero: "))

for i in range (1, n + 1):
    multiplo = 5 * i
    print (f"El numero {multiplo} es multiplo de 5")