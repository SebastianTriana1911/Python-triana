# Se crea una variable llamada "i" la cual se le asigna un valor de 1
i=1
# Se crea una variable llamada "sum" la cual se le asigna un valor de 0
sum=0
# Se crea un bucle while, cabe recalcar que los bucles while solo funcionan si la condicion que se le asigna es 
# verdadera "True" o simplemente se le coloca al lado del while el True y Python lo toma como que el bucle ya
# fuera verdadero, en el ejercicio podemos ver que al bucle while se le asigna una condicion la cual es que 
# i <= 5 lo que quiere decir que, si se cumple la condicion ya que 1 es menor a 5 por consiguiente el bucle 
# es verdadero y podra ejecutarse las siguientes lineas de codigo 
while i<=5:
    # Se le asigna la tarea de mostrar en pantalla el valor de "i"
    print(i)
    # Se asigna a la variable "sum" el resultado entre la suma del valor de la variable "sum" y la variable "i"
    sum=sum+i
    # Se asigna a la variable "i" la suma del valor de "i" + 1, cuando la variable "i" llegue a ser mayor que 5
    # el bucle parara
    i+=1 #i=i+1 
# El print en esta posicion quiere decir que ya no es parte del bucle while si no que cuando el bucle while pare
# ahi si se poder ejecutar esta linea de codigo, donde dice que muestre la suma de todos los numeros del 1 al 5.
print(f'la suma es ={sum}')