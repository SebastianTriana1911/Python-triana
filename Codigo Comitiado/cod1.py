# Se asigna a la variable "x" el numero que ingrese el usuario por consola  
x=int(input('ingrese numero')) 
# Se asigna a la variable "y" el numero que ingrese el usuario por consola 
y=int(input('ingrese numero'))
# Se asigna a la variable "x" el numero que ingrese el usuario por consola 
z=int(input('ingrese numero'))

# Se crea una funcion if donde si el valor de la variable "x" es mayor al valor de la variable "y" haga:
if x>y:
    # Haga otra funcion. Como ya sabemos que "x" es mayor a "y" entonces comprovemos si "x"
    # es mayor a "z" 
    if x>z: 
        # Si "x" es mayor a "z" se imprimira el valor que tenga la variable "x"
        print(f'el mayor es {x}') 
    else:
        # Si "x" no es mayor a "z" lo llevara al else, como ya sabemos que "x" no es mayor
        # a "z" entonces imprimiran el valor de la variable "z" 
        print(f'el mayor es {z}') 
# El else en esta posicion significa que como no se cumplio la funcion if de la linea 9 ahora
# se tendra que ejecutar la funcion else de la linea 21
else: 
    # Se crea otra funcion desde la funcion else diciendole si "y" es mayor a "z" ya que en
    # la linea 9 se determino que "y" es mayor a "x"
    if y>z: 
        # Si "y" es mayor a "z" se mostrara el valor de la variable "y"
        print(f'el mayor es {y}') 
    # Se crea un else por si "y" no es mayor a "z" 
    else:
        # Si sucede esta condicion que "y" no es mayor a "z" lo que se mostrara es el valor
        # de la variable "z" 
        print(f'el mayor es {z}')