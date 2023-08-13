# El ejercicio 8 constara de un codigo que permita que un usuario ingrese un numero y la consola le 
# muestre los numeros del 1 al 10 multiplicados por el numero que ingreso

# Se pide por pantalla un numero
numero = int(input("Escriba el numero que va hacer el multiplicador: ")) 
# Se inicializa la variable resultado en 0
resultado = 0

# Se hace un bucle for que recorra de 1 a 10 para dicha operacion
for i in range (1,10 + 1):
    # La variable reultado se convertira en la resultado de la operacion de la variable i con la variable
    # numero
    resultado = i * numero
    
    # Se muestra el resultado de la operacion
    print(f"{numero} x {i} = {resultado}")