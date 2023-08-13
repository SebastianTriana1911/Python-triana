# Se creara una variable que se le asignara el valor 1
num1=1
# Se creara un bucle while donde la condicion es que si el valor de la variable "num1" es menor o igual a 1000, lo
# que evidentemente dara verdadero, podra ingresar al bucle
while num1 <=1000:
    # Se creara una nueva variable "i" inicializada en 1
    i=1
    # Se creara una nueva variable "sum" inicializada en 0
    sum=0
    # Ahora crearemos un nuevo bucle while donde la condicion es que si el valor de la variable "i" es menor al valor
    # de la variable "num1" podremos entrar al bucle 
    while i<num1:
        # Entrando al bucle declaramos una funcion donde la condicion sea que si el modulo del valor de la variable 
        # "num1" y la variable "i" es igual a 0 entonces debera hacer:
        if num1%i==0:
            # Debera agregarle a la variable "suma" su mismo valor mas el valor que tenga en ese momento la variable "i" 
            sum+=i
        # Si esa funcion se cumple se le asignara a la variable "i" a suma de su valor mas 1
        i+=1
    # Ahora declaramos otra funcion donde la condicion sera si la variable "num1" es igual a la variable "sum"
    if num1==sum:
        # Imprima por consola que el valor asignado en la variable "sum" es perfecto 
        print(f'{sum} es perfecto')
    # Despues de que se haya cumplido todo el procedimiento a la variable "num1" se le asignara su mismo valor mas 1
    num1+=1