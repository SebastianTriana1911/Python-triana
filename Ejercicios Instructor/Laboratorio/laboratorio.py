lista = []
diccionario = {}
archi = input ("Ingrese la ruta de su archivo: ")
archivo = open (archi, "r")

for texto in archivo:
    for letras in texto:
        l = letras.lower()
        lista.append (l)
lista.sort()
for letra in lista:
    if letra not in diccionario:
        diccionario [letra] = 1
    else:
        diccionario [letra] = diccionario [letra] + 1
key = " "
diccionario.pop (key, None)
for clave, valor in diccionario.items():
    print (f"{clave} -> {valor}")