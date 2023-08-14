# Escriba un algoritmo que sume los números ingresados por el usuario hasta que el usuario ingrese el número 0 
# (detener las preguntas ante este escenario).

sum = 0 
numero = int(input("Ingrese un numero: "))
if numero <= 0:
    print ("Para entrar al bucle es necesario un numero mayor a 0")
else:

    while numero != 0:
        sum = sum + numero
        numero = int(input("Ingrese nuevamente un numero: "))
        continue
    print ("Termino el bucle" )
    print (f"La suma de todos los numeros fue: {sum}")


