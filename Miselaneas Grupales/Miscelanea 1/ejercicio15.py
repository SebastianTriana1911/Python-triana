# Diseñar e implementar un programa que solicite a su usuario un valor no negativo n y visualice 
# la siguiente salida:

num = int(input("Ingrese un numero: "))
for i in range(num,0,-1):
    for a in range(1,i +1):
        print(a, end=" ")
    print()