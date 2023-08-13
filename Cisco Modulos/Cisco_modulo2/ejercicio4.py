# El ejercicio 4 constara de ver la diferencia entre asignarle a la funcion input() los valores enteros como int 
# o los valores flotantes como float() y no asignarle estos valores, veremos los diferentes resultados por consola

numero1 = int(input("Escribe un primer numero: "))  # Podemos ver que a la funcion input() se le asigno un valor int
numero2 = int(input("Escribe un segundo numero: ")) # lo que consta que el resultado sea un numero entero

resultado = numero1 + numero2 
print(resultado)

numero1 = float(input("Escribe un primer numero: ")) # Podemos ver que a la funcion input() se le asigno un valor
numero2 = float(input("Escribe un segundo numero: ")) # flotante lo que consta que el resultado sea un numero decimal

resultado = numero1 + numero2 
print(resultado)

numero1 = (input("Escribe un primer numero: ")) # Podemos ver que a la funcion input() no se le asigno ningun valor
numero2 = (input("Escribe un segundo numero: ")) # lo que consta que el resultado sea la union de los dos valores
                                                  # siempre y cuando se le asigne una operacion de suma
resultado = numero1 + numero2 
print(resultado)
