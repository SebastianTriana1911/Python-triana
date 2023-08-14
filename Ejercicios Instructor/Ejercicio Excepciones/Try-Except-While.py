# TRY - EXCEPT

# Se crea un try except
try:
    # A la variable num1 se le pasa un tipo de dato numerico, si se ingresa
    # Otro tipo de dato saldra un error de tipo ValueError, donce el except
    # Ya contiende dicho tipo de error a si que se mostrara el mensaje que 
    # Tenga dicho error
    num1 = int (input ("Ingrese un numero: "))
    # Se valida si num1 es menor a 0
    if num1 < 0:
        # Si num1 es menor a 0 se mandara un erro de tipo Exception para
        # Que muestre el mensaje correspondiente
        raise Exception
    
    # Sucede todo lo anteriormente mencionado
    num2 = int (input ("Ingrese un numero: "))
    if num2 < 0:
        raise Exception

    # Si no hay ningun error se realizara una divicion normal, si num1 o num2
    # Son igual a 0 se genara una excepcion de tipo ZeroDivisionError el cual
    # Cuenta con su mensaje respectivo 
    resultado = num1 // num2
    print (f"El resultado de la division es {resultado}")

except ValueError:
    print (f"El dato que ingreso no es un numero")
except ZeroDivisionError:
    print ("La division tiene un 0 y no se puede dividir entre 0")
except Exception:
    print ("Usted ingreso un dato negativo")

# WHILE
while True:
    num1 = int (input ("Ingrese un numero: "))
    num2 = int (input ("Ingrese un numero: "))

    if num1 <= 0 or num2 <= 0 :
        print ("Alguno de los dos numeros que ingreso es 0 o menor a 0, vuelva a ingresar los numeros")
        continue
    else:
        resultado = num1 // num2
        print (f"""El resultado de la division es:
{num1} // {num2} = {resultado}""")
        break