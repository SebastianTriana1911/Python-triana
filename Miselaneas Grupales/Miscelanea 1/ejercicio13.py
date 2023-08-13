# Solicitar al usuario un número de hasta 9 dígitos e imprimirlo en orden contrario. Ej. digito 6754 
# imprimo 4576

numero = int(input("Ingrese un numero hasta 9 digitos: "))

numero = int(str(numero)[::-1])

print (f"El numero invertido es: {numero}")