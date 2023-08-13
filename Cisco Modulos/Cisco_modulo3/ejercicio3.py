# El ejercicio 3 constara de un codigo que permita que un usuario ingrese un numero por consola y esta haga una
# lista de numeros desde el 1 hatas el numero que el usuario ingreso, diciendole si es multiplo de 2 o no lo es
# con el bucle while

# Se crea un contador inicializado en 0
i = 0
# Se pide por consola un numero
numero = int(input("Escriba un numero: "))

# Mientras que el contador sea menor al numero entrara al bucle y cuando sea mayor saldra de este
while i < numero:

    # El contador se le suma uno ya que es menor al numero ingresado por consola
    i += 1
    # Se asigna en una variable el resultado del contador por el modulo de 2
    resultado = i % 2

    # Si el resultado de la operacion anterior es igual a 0 se imprimira su mensaje respectivo 
    if resultado == 0:
        print("El numero", i , "si multiplo de 2")
    # Si el resultado es diferente a 0 se mostrara otro mensaje
    else:
        print("El numero", i , "no es multiplo de 2")