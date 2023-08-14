lista = []
diccionario = {}
# A una variable se le asigna la ruta de un archivo
archi = input ("Ingrese la ruta de su archivo: ")
# A una variable llamada archivo se abre dicho archivo con un open y se le pasa el 
# Modo de apertura de lectura r
archivo = open (archi, "r")

# Se itera el archivo con un for
for texto in archivo:
    # Se crea un for anidado que itere cada palabra que contenga el archivo
    for letras in texto:
        # A una variable se le asigna la variable que este iterando las palabras del
        # Archivo con el .lower() que ayuda a que cada letra se combiera en minuscula
        l = letras.lower()
        # Cada letra se ingresara a la lista previamente creada
        lista.append (l)
# Ya cuando se acabe los bucles se ordenara alfabeticamente cada uno de los caracteres
# Con la funcion .sort()
lista.sort()

# Se itera cada elemento de la lista con un for
for letra in lista:
    # Se valida si el elemento que esta en la lista no esta en el diccionario, si dicha 
    # Validacion es True al diccionario se le agrega como clave la letra que este en la
    # Iteracion y el valor sera 1 ya que se encontro 1 vez 
    if letra not in diccionario:
        diccionario [letra] = 1
    # Si la validacion es Falsa osea que dicho elemento de la lista si esta en el diccionario
    # Entonces al diccionario en la clave que se este iterando en ese momento se le suma el 
    # Valor que esta ya tenga mas 1 ya que se a encontrado nuevamente
    else:
        diccionario [letra] = diccionario [letra] + 1

# A una variable llamada key se le asigna un valor vacio
key = " "
# Como el diccionario cuenta los espacios como elemento entonces se elimina del diccionario dichos
# Espacios llamandole al diccionario el metodo pop() que permite elimina elementos, y se le pasa
# Como clave la variable key que es el elemento (Espacio) y como valor None
diccionario.pop (key, None)

# Ahora se iterara el diccionario mostrando la clave y el valor, para esto se itera el diccionario con 
# El metodo items()
for clave, valor in diccionario.items():
    # Se imprime por pantalla la clave y el valor que contenga el diccionario
    print (f"{clave} -> {valor}")