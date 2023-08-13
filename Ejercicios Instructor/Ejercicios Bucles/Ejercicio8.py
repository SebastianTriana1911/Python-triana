# While: Lea dos numeros. Garantice que hay uno mayor que el otro. Si no es el caso pidalos de nuevo. Reste el menor del
# mayor y si el resultado lo permite reste nuevamente. Diga cuanto sobra

resul = 0
num1=20
num2=20

while num1 == num2 or num2 == num1:
    num1 = int(input("Ingrese un numero: "))
    num2 = int(input("Ingrese un numero: "))

    if num1 > num2:
        resul = num1 - num2
        print (f"El resultado de la resta entre {num1} y {num2} es: {resul}")
    elif num2 > num1:
        resul = num2 - num1
        print (f"El resultado de la resta entre {num2} y {num1} es: {resul}")

    while resul != 0:
        if num1 < num2:
            resul = resul - num1
            print(f"El resultado {resul}")
        else:
            resul = resul - num2
            print(f"El resultado {resul}")     
        if resul <=0:
            print (f"Lo sobrante de la resta es {resul}")
            break
