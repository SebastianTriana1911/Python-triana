# Calcular el máximo de números positivos introducidos por teclado, sabiendo que metemos números hasta 
# que introduzcamos uno negativo. El negativo no cuenta.

# Se solicita un numero por teclado para asignarselo a la variable num
num = int(input("Ingrese un numero: "))
# Se inicializa cont en 0
cont = 0

# Si el numero ingresado es mayor a 0 entra al bucle
while num > 0:
    # Cont se le suma 1
    cont = cont + 1
    # Se le pide al usuario que ingrese otro numero y se vuelve a validar en el bucle While si este es
    # Mayor a 0 si no es asi se le dira por pantalla cuantos numero ingreso
    num = int(input("Ingrese un numero: "))
print (f"La cantidad de numeros introduciodos es de {cont}")
