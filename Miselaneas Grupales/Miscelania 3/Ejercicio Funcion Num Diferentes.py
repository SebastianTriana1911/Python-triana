# Llenar un arreglo de n elementos con números generados con la función random. No puede haber números repetidos. 
# Si intenta ingresar al arreglo un número que ya existe, imprimirlo para anunciar que ese número ya está en el 
# arreglo.
import random

def lista_numeros_diferentes ():
    lista = []
    cont = 0
    tam = random.randint(10,20)
    for i in range (tam):
        cont = cont + 1
        numero = random.randrange(10,30)
        if numero not in lista:
            lista.append(numero)
        else:
            print (f"El numero {numero} ya se encuentra en la lista, vuelta {cont}")
    return lista
lista2 = lista_numeros_diferentes ()
print (lista2)

