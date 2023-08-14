# Escriba un algoritmo que sume los números ingresados por el usuario y cuando la suma sea superior a 100 deje de
# pedir números y muestre el total.

sum = 0 
numero = int(input("Ingrese un numero: "))
if numero <= 0:
    print ("Para entrar al bucle es necesario un numero mayor a 0")
else:
    while True:
        sum = sum + numero
        if sum >= 100:
            print (f"La suma de todos los numeros fue: {sum}")
            break
        else:
            numero = int(input("Ingrese nuevamente un numero: "))
            continue

    
    
     
    #while numero != 0:
        #sum = sum + numero
        #numero = int(input("Ingrese nuevamente un numero: "))
        #continue
    #print ("Termino el bucle" )
    #print (f"La suma de todos los numeros fue: {sum}")
