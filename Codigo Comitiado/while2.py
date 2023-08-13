# Se crean dos variables "x" y "y" donde se le asignan dos valores a cada una separados por una coma 3 y 5 
x,y=3,5
# Se crea la variable "cont" con un valor de 1
cont=1
# Se crea un bucle while y hasta que sea verdadera iniciara como los argumentos insertados al lado del while no son verdaderos no iniciara 
# el bucle por esa razon es que se encierran en parentesis y al lado izquierdo se le asigna la funcion not que esta lo que quiere decir es
# que invierte el False de los argumentos encerrados a un True permitiendo la entrada al bucle 
while not(x%y==0 or y%x==0):
    # Se asigna un print que muestre el valor de la variable "cont" y esos seran los intentos que a realizado para salir del bucle 
    print(f'intento numero {cont}')
    # A la variable "x" se le asigna el nuevo valor que vaya a ingresar el usuario por consola 
    x=int(input('ingrese numero'))
    # A la variable "y" se le asigna el nuevo valor que vaya a ingresar el usuario por consola
    y=int(input('ingrese numero'))
    # A la variable "cont" se le sumara 1, esto sucedera cada que el usuario no ingrese dos numeros que sean factores del otro, si no lo son 
    # seguira en el bucle haciendo que la variable "cont" vaya subiendo de 1 en 1 y mostrandole en la linea 10 cuantos intentos lleva 
    # gracias a esta linea de codigo 
    cont+=1

# Si el usuario ingresa dos numeros que sean factores saldra del bucle por eso es que este print esta afuera, por que solo se ejecutara cuando
# salga del bucle, y si es asi mostrara el valor de la variable "x" y "y" seguido de la cadena de texto "son factores"
print(f'{x} y {y} son factor')