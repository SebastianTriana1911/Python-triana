# Calcular la operación x n sin utilizar la función pow

# Se solicita por consola dos numero que representaran la base y el exponente
# Para realizar una potencia
x = int(input("Ingrese la base de la potencia: "))
n = int(input("Ingrese el exponente de la potencia: "))

# A una variable reultado se le asigna el resultado de la potencia de estos dos
# Numeros con el operador **
resultado = x ** n

# Se imprime el resultado de dicha potencia
print (f"El resultado de la potencia entre {x} elevado a {n} es: {resultado}")