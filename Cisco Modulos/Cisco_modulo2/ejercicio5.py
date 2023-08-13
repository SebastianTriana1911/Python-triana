# El ejercicio 5 constara de un codigo donde se le pida a un usuario dos numeros, el codigo hara que esos dos
# numeros realizen una division y que el cociente de esa division se eleve al cuadrado, mostrando en consola el resultado 

numero1 = int(input("Escriba el primer numero: "))
numero2 = int(input("Escriba el segundo numero: "))

cociente = numero1 % numero2 # El simbolo %  significa que hara una division entre los dos numeros y mostrara el cociente 

print("El cociente de la division de los dos numeros que digito fue:", cociente)

resultado = cociente ** 2 # El simbolo ** significa la potencia entre dos numeros 

print("El resultado del cociente de la division anterior elevado al cuadrado fue: ", resultado)