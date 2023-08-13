# Escribir un programa que visualice la siguiente figura, utilizando ciclos. El usuario decide cuantas
# líneas quiere imprimir
# *
# * *
# * * *
# * * * *
# * * * * *       
# * * * * * *
# * * * * * * *
# * * * * * * * *
# * * * * * * * * *

limite = int(input("Ingrese cuuantas lineas quiere imprimir: "))

for i in range(0, limite):
    for j in range(0, i+1):
        print("* ",end="")
    print()
