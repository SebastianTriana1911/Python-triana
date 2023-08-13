# Algoritmo para hallar el m.c.d de dos números m y n por el algoritmo de Euclides.

# Se pide por consola 2 numeros que sera el primero el divisor y el segundo el dividendo
divisor = int(input("Ingrese el numero que desee que sea divisor: "))
dividendo = int(input("Ingrese el numero que desee que sea dividendo: "))
# Se inicializa una variable auxiliar en 0
aux = 0
# Si a la hora de ingresar el dividendo y este es 0 no entrara al bucle
while dividendo != 0:
    # De lo contrario a la variable aux se le asigna el valor que tiene dividendo
    aux = dividendo
    # Dividendo cabiara su valor por la operacion del modulo del divisor por el dividendo
    dividendo = divisor % dividendo
    # Al divisor se le asigna el valor que aux que fue el numero que se ingreso para la variable
    # dividendo
    divisor = aux
# Se imprime por pantalla el maximo comun divisor de los numeros que se ingresaron
print (f"El maximo comun divisor es: {divisor}")