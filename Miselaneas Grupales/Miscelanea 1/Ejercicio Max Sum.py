# Encontrar un número natural n más pequeño tal que la suma de los n primeros números naturales 
# (1 + 2 + 3 + 4.....) exceda de una cantidad (máximo) introducida por el teclado. Es decir cuantos números
# de la serie de los naturales debo sumar para superar el dato máximo.

# Se solicita un numero por consola
maximo = int(input("Introdusca el dato maximo: "))
# Se inicializa la variable suma en 0
suma = 0 

# Se itera en un bucle for la variable i que recorrera 1 hasta el numero que se ingreso por consola
for i in range (1, maximo + 1):
    # Por cada iteracion se ira sumando el valor de suma mas lo que tenga asignado la variable i en su momento
    suma = suma + i
print(suma)