# Llenar un arreglo con la serie de Fibonacci, con la cantidad de dígitos que el usuario indique al inicio del 
# programa.

# Se crea una lista
lista = []
# Se le asigna un numero a la variable numero_final
numero_final = int(input("Ingrese en numero que indique el final de la lista: "))
# La variable num1 se inicializa en 0 ya que este se debera sumar con la variable num2 y este resultado tendra 
# Que dar 1 ya que la serie de fibonnacci empieza desde el 1
num1 = 0
# Se inicializa la variable num2 en 1 
num2 = 1
# La variable i recorrera desde 1 hasta numero_final
for i in range (numero_final):
    # La variable result contendra el resultado de la suma entre el num1 y num2
    result = num1 + num2
    # Num1 cambia su valor por el que tenia num2 ya que el ultimo numero debera ser sumado entre el resultado de
    # la suma anterior
    num1 = num2
    # Num2 se le asigna el valor que tiene la variable result para poder hacer la suma anteriormente vista, pero ahora
    # Sera el ultimo numero sumado entre el resultado de la suma entre el primer numero y segundo numero
    num2 = result
    # El valor de la variable result se inserta en la lista para ver el resultado final dentro de esta
    lista.append(result)
print (lista)

