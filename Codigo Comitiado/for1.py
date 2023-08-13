# Cuando vamos a tulizar el ciclo for debemos asignarle una variable segido de in range luego de eso abriremos parentesis y si insertamos
# solo un argumento nos indicara el pundo a donde se termina el ciclo
for i in range(11):
    
    # La funcion if nos indica que si el residuo del numero que le corresponde a la variable "i" dividido entre 3 es igual a 0  
    if i%3==0:
        
        # Debera imprimir en pantalla que el numero de la variable "i" es multiplo de 3
        print(f'{i} es multiplo de 3')
    # Se asigna un else por si no se cumple la funcion de if
    else:
        # Si la variable i no es multiplo de 3 osea no cumple la condicion del if entonces debera solo imprimir el numero
        print(i)

# Cuando queremos iniciar desde un numero y terminar en otro numero ya preestablecido deberemos colocar dos valores separados por comas entre
# los parentecis de range, el primer valor que se le asigna ahora sera el punto de partido y el segundo nos dire el
# numero en el que queremos que termine el ciclo
for j in range(1,11):

    # Nos mostrara por consola todos los numeros desde el 1 hasta el 11 en este caso
    print(j)

# Si queremos colocar una cantidad preestablecida para que vaya aumentando el contador lo asignamos en el 3 valor, esto quiere
# decir que el primer valor significa el punto de partida del ciclo, el segundo valor significa en que numero donde va a terminar el ciclo,
# y el tercer valor significa la cantidad de numeros que va aumentar para mostrar el siguiente numero
for k in range(0,11,2):
    
    # Nos mostrara por consola un contador desde 1 aumentando de 2 en 2 hasta 11
    print(k)

# Cuando el tercer valor es negativo quiere decir que en este caso va a disminuir de dos en dos, para lograr que el codigo funciones como lo esperado
# esto el primer valor osea el valor que indica el punto de partida tiene que ser mayor al valor que indica el final, si esto no es asi no se
# ejecutara el codigo
for i in range(20,0,-2):
    # Ahora se le esta indicando que muestre el valor de la variable "i" en este caso mostrara todos los valores hasta 20 pero como el ciclo nos esta
    # indicando que tiene que ser de 20 para abajo entonces mostrara esa lista de numeros disminuyendo de dos en dos  
    print(i)