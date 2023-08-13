# Determine cuales y cuantos numeros perfectos hay entre 1 y 1000

# Se le asignan dos variables perf y cont en 0
perf = 0
cont = 0

# Se hace un bucle que itere de 1 a 1000 y dicho valor lo llevara la variable i
for i in range (1,1000):
    # La variable perf como cambiara su valor mas adelante se inicializa en 0 en 
    # Este punto para que en la proxima iteracion del siguiente bucle pueda sumarse
    # desde 0
    perf = 0

    # Se itera 1 hasta lo que valga la variable i y se guardara cada iteracion en la
    # Variable a
    for a in range (1,i):
        # La variable resultado guardara el resultado de lo que vale la variable i por el
        # Modulo de lo que vale la variable a
        resultado = i % a 
        # Se valida si el resultado es igual a 0, si esto es verdadero la variable perf se
        # suma 1
        if resultado == 0:
            perf = perf + a

    # Ya acabado el bucle anidado se valida donde si perf es igual al valor de i, si esto es
    # Verdadero hay un numero perfecto y se muestra por pantalla y se suma 1 a la variable cont
    # Para que al final de todas las iteraciones se muestre la cantidad de numero perfectos que
    # Se logro encontrar
    if perf == i:
        cont = cont + 1
        print (f"El numero {i} es perfecto")
        
print(f"Hay una cantidad de {cont} numeros perfectos")
    