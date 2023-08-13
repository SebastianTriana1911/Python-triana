import random
lista = []
tam = random.randint(15, 20)
cont1 = 0
lista2 = []   

# Iterarcada de 1 hasta el numero que tiene la variable tam echa por random.randint
for i in range(tam):
    num= random.randrange(0,9)
    lista.append(num)    
print(lista)

# Pedir un numero por consola para ver si se encuentra entre la lista
numero = int(input("Ingrese un numero: "))
# Se valida por medio del bucle while si no esta el numero ingresado en la lista, si este
# No esta en la lista se tendra que infresar otro hasta que coinsida con algun numero que
# Este en la lista
while numero not in lista:
    numero = int(input("Ingrese un numero: "))

# Si el numero que se ingreso si esta en la lista se imprime que si esta
if numero in lista:
    print(f"El numero {numero} si esta")    


for n in lista:
    cont=0
    for j in lista:
        posicion = cont1
        if numero == j:
            lista2.append(posicion)
        cont1 += 1
        if posicion > tam:
            break     

for n in lista:
    cont=0
    for j in lista:
        posicion = cont1
        if numero == j:
            cont+=1
if cont == 1:
    print(f"El numero {numero} no se repite")            
print(f"El numero {numero} esta {cont} veces")

for s in lista2:
    indice = s
    print(f"El numero {numero} se encontro en la posicion {indice}")