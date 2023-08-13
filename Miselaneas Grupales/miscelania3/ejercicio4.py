# Llenar un arreglo de n elementos con números generados con la función random. Cada número siguiente debe ser mayor que el
# anterior, pero no puede exceder el valor de la siguiente decena.
import random

lista = []
tam = 5
aux = 0
numero = 0
acum = 0
aux = 0
for i in range (tam):
    numero = random.randrange(5,50)
    print (f"El numero es {numero}")
    if numero >= aux:
        decena = numero + 10
        print (f"Decena del {numero} es {decena}")
    if numero >= aux and numero <= decena:
        lista.append(numero)
        aux = numero
    
print (lista)
