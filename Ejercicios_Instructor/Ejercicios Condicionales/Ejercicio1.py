# El ejercicio 1 consta de un codigo que haga un bucle del 1 al 10 y haga la suma de todos los numeros pares y por
# aparte la suma de todos los numeros impares 

i = 0
par = 0
impar = 0

for i in range (0,10):
    i = i + 1
    resultado = i % 2
    if resultado == 0:
     par = par + i 

    elif resultado != 0:
       impar = impar + i

print (f"La suma de los numeros pares es: {par}")
print(f"La suma de los numeros impares es: {impar}")
    