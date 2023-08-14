# Escriba un programa que simule una hucha. El programa solicitará primero una cantidad, que será la cantidad de 
# dinero que queremos ahorrar. A continuación, el programa solicitará una y otra vez las cantidades que se irán 
# ahorrando, hasta que el total ahorrado iguale o supere al objetivo. El programa no comprobará que las cantidades
# sean positivas.

ahorro = 0
cantidad = float(input("Cuanto dinero desea ahorrar: "))
if cantidad < 0:
    print ("Se deaea que ingrese un numero mayor a 0")
else:
    while True:
        cont = float(input("Cuanto desea ahorrar hoy: "))
        ahorro = ahorro + cont
        if ahorro >= cantidad:
            print(f"Usted a ahorrado {ahorro} significa que ya ahorro lo que deseaba")
            break
        else:
            continue
