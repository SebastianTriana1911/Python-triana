# Se asigna a la variable "n" el valor que el usuario va a ingresar
n=int(input('ingrese numero'))
# Se asigna a variable "i" el valor 1
i=1
# Se crea un bucle donde si el valor asignado a la variable "i" es menor al numero que ingreso el usuario por pantalla se ejecute
while i<n:
    # Si ya estamos en el bucle es por que la condicion fue verdadera entonces le asignamos una funcion donde si el valor de "i" dividida
    # entre 7 tiene un residuo igual a 0 
    if i%7==0:    
        # Tendra que imprimir que el valor de "i" es multiplo de 7
        print(f'{i} es multiplo de 7')
    # Si el residuo de la el valor de "i" entre 7 no da un reiduo 0 se creara otra funcion que sera else donde 
    else:
        # Tendra que imprimir el valor que tenga actualmente "i"
        print(i)
    # El valor de "i" se le aumentara 1 hasta que sea igual a el numero ingresado por el usuario, si eso pasa saldra del bucle
    i+=1