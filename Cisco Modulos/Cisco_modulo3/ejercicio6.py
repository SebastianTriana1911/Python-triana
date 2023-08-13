# El ejercicio 6 constara de un codigo que permita que un usuario pueda realizar una operacion basica ingresando
# los dos numeros que quiere operar y la consola le muestre el resultado

# Se pide en dos variable dos numero 
numero1 = int(input("Escriba el primero numero que desea operar: "))
numero2 = int(input("Escriba el segundo numero que desea operar: "))

# Se inicia un bucle inicializado en True
while True:
    #Se solicita por consola que esriba la operacion que desea realizar
    a = input("Escriba que operacion desea realizar: suma, resta, multiplicacion, division, potenciacion: ")

    # Se valida lo que se ingreso por pantalla con las diferentes operaciones que se podrian realizar, si la variable
    # que guardo lo que se ingreso por pantalla es igual a alguna de las operaciones se mostrara el resultado 
    # correspondiente, si no corresponde con ninguna de las operaciones se volvera a preguntar
    if a == "suma":
        b = numero1 + numero2 
        print ("La suma entre", numero1 , "y", numero2 , "fue: ",b)
        break

    elif a == "resta":
        b = numero1 - numero2 
        print ("La resta entre", numero1 , "y", numero2 , "fue: ",b)
        break

    elif a == "multiplicacion":
        b = numero1 * numero2 
        print ("La multiplicacion entre", numero1 , "y", numero2 , "fue: ",b)
        break

    elif a == "division":
        b = numero1 / numero2 
        print ("La division entre", numero1 , "y", numero2 , "fue: ",b)
        break

    elif a == "potenciacion":
        b = numero1 ** numero2 
        print ("La potencia entre", numero1 , "y", numero2 , "fue: ",b)
        break
    else: 
        print("Usted ingreso el nombre de la operacion mal por favor vuelva e ingreselo")