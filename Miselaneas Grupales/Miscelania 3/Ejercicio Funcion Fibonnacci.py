# Llenar un arreglo con la serie de Fibonacci, con la cantidad de dígitos que el usuario indique al inicio del 
# programa.

def fibonacci ():
    lista1 = []
    result = 0
    numero_final = int(input("Ingrese en numero que indique el final de la lista: "))
    num1 = 0
    num2 = 1
    for i in range (numero_final):
        result = num1 + num2
        num1 = num2
        num2 = result
        lista1.append(result)
    return f"{lista1}"
lista = fibonacci()

print (lista)

