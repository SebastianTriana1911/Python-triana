# Se crean dos variables separadas por coma, con dos valores separados por comas, esto quiere decir que el primer
# valor es asignado a la primera variable y el segundo valor va asignado a la segunda variable 
num1,num2=100,50
# Se imprimen varios mensajes haciendo que en la consola se visualice una lista de operaciones numeradas para que mas
# adelante en un input el usuario pueda ingresar el numero segun la operacion que desee realizar  
print('1-sumar')
print('2-restar')
print('3-multiplicar')
print('4-dividir')
print('5-residuo')
# Se crea la variable "op" para guardar el numero que ingreso el usuario dependiendo de la operacion que haya escogido
op=int(input('que operacion?'))
# Se asigna una funcion match la cual es una manera mas corta y mas sencilla de trabajar las funciones if - elif - 
# else, la funcion match case nos permite buscar todos los casos posibles segun la variable asignada con el match,
# si dicha variable llega hacer match osea llega a coincidir con un case se ejecutara el codigo que tenga ese case
match op:
    # Case 1, significa que si el usuario ingresa a la variable "op" el numero 1, entonces la variable "op" hizo match con
    # case 1 ya que a case se le asigno el valor 1 entonces si el valor de "op" y el valor de case son iguales se hira
    # por ese case 
    case 1:
        # Siendo "op" igual a case 1 se le esta diciendo que muestre por pantalla la suma entre el valor asignado en 
        # la variable "num1" y "num2" por que como vimos anteriormete si el usuario marcaba un numero se le asignaba
        # la operacion que tuviera dicho numero y al numero 1 se le asigno la operacion suma 
        print(num1+num2)
    # Se crea otro case para otra posible respuesta del usuario, por consiguiente un valor nuevo a la variable "op",
    # como al case se le asigno el numero 2, entonces si op = 2 se vendra por este case  
    case 2:
        # Ya que op = case 2 se le esta diciendo que muestre la resta entre los valores de la variable "num1" y "num2"
        print(num1-num2)
    # Se crea otro case para otra posible respuesta del usuario, por consiguiente un valor nuevo a la variable op,
    # como al case se le asigno el numero 3, entonces si op = 3 se vendra por este case 
    case 3:
        # Ya que op = case 3 se le esta diciendo que muestre la multiplicacion entre los valores de la variable "num1"
        # y "num2"  ya que la multiplicacion se le habia asignado el numero 3 
        print(num1*num2)
    # Se crea otro case para otra posible respuesta del usuario, por consiguiente un valor nuevo a la variable op,
    # como al case se le asigno el numero 4, entonces si op = 4 se vendra por este case   
    case 4:
        # Ya que op = case 4 se le esta diciendo que muestre la division entre los valores de la variable "num1"
        # y "num2" ya que a la division se le habia asignado el numero 4 
        print(num1/num2)# //  /
    # Se crea otro case para otra posible respuesta del usuario, por consiguiente un valor nuevo a la variable op,
    # como al case se le asigno el numero 5, entonces si op = 5 se vendra por este case     
    case 5:    
        # Ya que op = case 5 se le esta diciendo que muestre el residuo de la division entre los valores de la variable "num1"
        # y "num2" ya que al residuo o mod se le habia asignado el numero 5 
        print(num1%num2)