# TRY - EXCEPT
try:
    num1 = int (input ("Ingrese un numero: "))
    if num1 < 0:
        raise Exception
        
    num2 = int (input ("Ingrese un numero: "))
    if num2 < 0:
        raise Exception

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