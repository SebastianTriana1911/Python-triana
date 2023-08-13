# Algoritmo para hallar el m.c.d de dos números m y n por el algoritmo de Euclides.
divisor = int(input("Ingrese el numero que desee que sea divisor: "))
dividendo = int(input("Ingrese el numero que desee que sea dividendo: "))

aux = 0
while dividendo != 0:
    aux = dividendo
    dividendo = divisor % dividendo
    divisor = aux
print (f"El maximo comun divisor es: {divisor}")