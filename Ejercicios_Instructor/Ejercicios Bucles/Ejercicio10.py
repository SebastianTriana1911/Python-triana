# Solicite un numero positivo al usuario ( debe incluirse en la serie ). Diga cuantos multiplos de n hay en la 
# serie desde cero hasta el numero ingresado. n se ingresa por teclado tambien

fin = int(input("Ingrese el numero en el que desea terminar la lista: "))
n = int(input("Ingrese un numero positivo: "))
x = 0

for i in range (0,fin+1):
    print (i)
    if i % n == 0:
        print(f"El numero {i} es multiplo de {n}")
        x = x + 1
print (f"\nLa cantidad de multiplos encontrados fue: {x}")

