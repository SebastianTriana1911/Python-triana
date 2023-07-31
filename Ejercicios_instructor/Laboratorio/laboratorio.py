abecedario = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "ñ",
                "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
diccionario = {}
diccionario2 = {}
try:
    # archivo = input ("Ingrese la direccion del archivo de entrada: ")
    archivo2 = open ("C:\\Users\\Sebastian\\OneDrive\\Escritorio\\Sena\\Instructor Sumuel\\laboratorio.txt", 'rt')
    for key in abecedario:
        diccionario [key] = " "
    for i in archivo2:
        cont = 0
        for a in i:
            letra = a.lower()
            for clave in diccionario:
                if letra == clave:
                    print (clave)
                    print (f"a {letra}")
                    cont = cont + 1
                    valor = cont
                    diccionario2 [clave] = valor
        for clave,valor in diccionario2.items():
            print (clave,"->",valor)
    archivo2.close ()
except:
    print ("A surgido un error")
