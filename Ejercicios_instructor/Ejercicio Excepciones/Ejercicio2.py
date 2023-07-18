# TRY - EXCEPT 
import math
try:
    a = int ( input ("Ingrese el valor que va a tomar a: "))
    b = int ( input ("Ingrese el valor que va a tomar b: "))
    c = int ( input ("Ingrese el valor que va a tomar c: "))
    if a == 0 or b == 0 or c == 0:
        raise ArithmeticError
    rb = (b ** 2) 
    r = ((-4 * a) * c)
    print ("""\nQue desea ver
1. Suma 
2. Resta
""" )
     
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
            
except ArithmeticError:
    print ("El ejercicio debe constar de numeros mayores a 0")
except Exception:
    print ("No se le puede sacar raiz a un numero menor o igual a 0 ")