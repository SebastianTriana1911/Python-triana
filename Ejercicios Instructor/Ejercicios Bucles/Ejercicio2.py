# Escriba un algoritmo que lea del teclado un número entero y que compruebe si el número es menor que 10. Si no lo
# está, debe volver a leer el número repitiendo la operación hasta que el usuario escriba un valor correcto. 
# Finalmente, debe escribir por pantalla el valor leído cuando este sea correcto.

while True:
    numero = int( input("Escriba un numero menor que 10: "))
    if numero < 10:
        print (f"El numero {numero} es menor que 10")
        break
    else :
        print (f"El numero {numero} no es menor que 10")
        continue 