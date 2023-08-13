# Solicitar al usuario un número de hasta 9 dígitos e imprimirlo en orden contrario. Ej. digito 6754 
# imprimo 4576

# Se pide por consola un numero
numero = int(input("Ingrese un numero hasta 9 digitos: "))

# La variable que contiene ese numero se le saca en rebanada de una manera negativa para que este invierta su valor 
numero = int(str(numero)[::-1])

# Se imprime el numero en inversa
print (f"El numero invertido es: {numero}")