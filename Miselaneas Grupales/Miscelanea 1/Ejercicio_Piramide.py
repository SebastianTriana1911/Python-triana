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

# Se ingresa un numero por teclado que determinara la cantidad de columnas que tendra la piramide
limite = int(input("Ingrese cuuantas lineas quiere imprimir: "))

# Se itera por una variable i del numero 0 hasta el numero ingresado  
for i in range(0, limite):
    # Se itera por una variable j dese el numero 0 hasta el valor que tenga la variable i
    for j in range(0, i+1):
        # Se imprime *  por cada iteracion que tenga j, si j tiene mas de una iteracion se asigna
        # La palabra reservada end="", que permite que cada iteracion que tenga j se imprima en una
        # Misma linea
        print("* ", end="")
    # Salta una linea ya que si no se coloca seguira imprimiendo en una linea de recorrido
    print()
