# El ejercicio 7 constara de un codigo que permita que un usuario pueda insertar un numero positivo
# por consola y esta le mostrara la secuencia de ese numero hasta 0

# Se solicita un numero por pantalla
numero = int(input("Escriba un numero que sea positivo: "))

# Dicho numero se iterara por un bucle for que empieze desde el numero ingresado y este ira hasta -1
# para que vaya hasta 0 y este se iterara de uno en uno, hasta llegar a 0
for i in range(numero,-1,-1):
    # Se imprime la variable que guarda dicha iteracion
    print(i)