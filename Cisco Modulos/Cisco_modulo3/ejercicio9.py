# El ejercicio 9 constara de un codigo donde un usuario ingrese dos numeros por consola listandole todos los numeros
# desde el primero hasta el segundo diciendole cuales son par y cuales no 

# Se pide por pantalla dos numeros el primero siendo cualquier numero positivo entero y el siguiente que sea mayor al
# Anterior numero ingresado
numero1 = int(input("Escriba un numero entero: "))
numero2 = int(input(f"Escriba un numero mayor a {numero1}: "))
# Se inicializa una variable resultado en 0
resultado = 0

# Se valida con la constante if si el segundo numero es menor al primer numero que se ingreso por pantalla
if numero2 < numero1:
      # Si esta validacion es True se mostrara un mensaje
      print (f"¡Le he pedido un número mayor o igual que {numero1} !")
# De lo contrario se iterara en un blucle for el primer numero hasta llegar al segundo numero 
else:
      for i in range (numero1, numero2 + 1):
            # A la variable resultado se le asigna el resultado de lo que valga la variable i con el modulo de 2
            resultado = i % 2
            # Si el valor de la variable es igual a 0 es por que el el valor de la variable i es par de lo contrario
            # Se imprimira que no lo es
            if resultado == 0:
             print (f"El numero {i} es par")      
            else:
                  print (f"El numero {i} es impar") 
                
