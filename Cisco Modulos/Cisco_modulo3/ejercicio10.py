# El ejercicio 10 constara de un codigo donde el usuario pueda ingresar una palabra y pueda ingresar el numero de 
# veces que quiera que esta se visualize en la consola 

# Se solicitan en dos variables una palabra y el numero de veces que se desea que se muestre en pantalla dicha palabra
palabra = input("Escriba una palabra: ")
veces = int(input("Escriba el numero de veces que desea ver la palabra "))

# Se itera el numero de veces que el usuario desea ver la palabra por cada vuelta que haga se mostrara la palabra
for i in range(veces):
    print(palabra)