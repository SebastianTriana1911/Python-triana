# ¿Cuáles y cuántos son los números primos comprendidos entre 1 y 1000?

result = 0
cont = 0
cont2 = 0
for i in range (1,10 + 1):
    cont = 0
    for a in range (1,i + 1):
        result = i % a
        if result == 0:
            cont = cont + 1
    if cont <= 3:
        cont2 = cont2 + 1
        print (f"El numero {i} es primo")

print (f"Hay una cantidad de {cont2} numeros primos")