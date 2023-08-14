# TRY - EXCEPT 

# Se importa la funcion math para operaciones matematicas
import math

# Se crea un try para sobreponerse a cualquier error
try:
    # A tres variables se les asigna un tipo de dato numerico
    a = int ( input ("Ingrese el valor que va a tomar a: "))
    b = int ( input ("Ingrese el valor que va a tomar b: "))
    c = int ( input ("Ingrese el valor que va a tomar c: "))
    # Se valida si alguna de estas variables es igual a 0
    if a == 0 or b == 0 or c == 0:
        # Si ela validacion es verdadera se manda una exepcion ArithmeticError
        # Con la palabra reservada raise
        raise ArithmeticError
    # Si la validacion es False se realiza la operacion de la funcion cuadratica
    rb = (b ** 2) 
    r = ((-4 * a) * c)
    # Como en un punto de la funcion cuadratica hay un mas y un menos se pregunta que
    # Que operacion desea hacer
    print ("""\nQue desea ver
1. Suma 
2. Resta
""" )
    
    # Segun la opcion que haya escogido el usuario se hace su respectiva operacion sea suma o resta
    opcion = int (input ("Ingrese el numero que le corresponda a la ocion que desea ver: "))
    match opcion:
        case 1:
            if r < 0:
                result = rb + r
                raiz = math.sqrt(result)
            if raiz < 0:
                raise Exception
            else:
                suma = (b * -1) + raiz 
                resultado = suma // (2 ** a)
                print (f"La funcion cuadratica con suma es: {resultado}")
        case 2:
            if r > 0:
                result = rb + r
                raiz = math.sqrt(result)
            if raiz < 0:
                raise Exception
            else:
                resta = (b * -1) - raiz 
                resultado = resta // (2 ** a)
                print (f"La funcion cuadratica con resta es: {resultado}")

# Si se manda algun error por la palabra reservada raise se mostrara el mensaje que 
# Cada exepcion cuente, cada exepcion tiene un tipo de error y ese tipo de error tiene
# Un mensaje especifico para mostrar, (Si se desea colocar except que contengan un error
# Especifico es importante que a lo ultimo vaya el except mas general)
except ArithmeticError:
    print ("El ejercicio debe constar de numeros mayores a 0")
except Exception:
    print ("No se le puede sacar raiz a un numero menor o igual a 0 ")