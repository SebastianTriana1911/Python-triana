# Hacer diccionarios español ingles, ingles español de animales. Escriba funciones que permitan alimentar
# estos diccionarios y usarlos. Genere un menú para cada una de las 4 opciones. Alimentar cada diccionario
# (2 funciones) Usar cada diccionario (2 funciones)

diccEspañol = {}
diccIngles = {}
diccUsuario = {}

def españolIngles (reps,clave,valor,diccionario):
    diccionario.update({clave:valor})
    for i in range (1, reps):
        clave = input("Escriba la clave en español: ")
        valor = input("Escriba el valor en ingles: ")
        diccionario.update({clave:valor})
    return diccionario
print(españolIngles(int(input("Cuanteas veces desea llenan el diccionario: ")), input("Escriba la clave en español: "), input("Escriba el valor en ingles: "), diccEspañol))

def inglesEspañol (reps,clave,valor,diccionario):
    diccionario.update({clave:valor})
    for i in range (1, reps):
        clave = input("Escriba la clave en ingles: ")
        valor = input("Escriba el valor en español: ")
        diccionario.update({clave:valor})
    return diccionario
print(inglesEspañol(int(input("Cuanteas veces desea llenan el diccionario: ")), input("Escriba la clave en ingles: "), input("Escriba el valor en español: "), diccIngles))

print (f"\nMenu Diccionarios\n")
print (f"1. Ingles a Español")
print (f"2. Español a Ingles\n")
respuesta = int(input("Con que funcion desea llenar su diccionario: "))
if respuesta == 1:
    print(inglesEspañol(int(input("Cuanteas veces desea llenan el diccionario: ")), input("Escriba la clave en ingles: "), input("Escriba el valor en español: "), diccUsuario))
elif respuesta == 2:
    print(españolIngles(int(input("Cuanteas veces desea llenan el diccionario: ")), input("Escriba la clave en español: "), input("Escriba el valor en ingles: "), diccUsuario))
else:
    print (f"La opccion que escogio no esta dentro del menu")

# Codifique funciones para alamacenar en tuplas de cada diccionario todos los animales en español y en ingles respectivamente. 
def diccTuplas (diccionario):
    tupla = diccionario.items()
    return tupla
print (diccTuplas(diccEspañol))
print (diccTuplas(diccIngles))
print (diccTuplas(diccUsuario))
