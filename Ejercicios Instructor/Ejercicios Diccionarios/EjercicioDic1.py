# Funcion Recibe un diccionario y una palabra que representa la clave (key), y nos retorna el valor 
# asociado y el tipo de dato de ese valor. Si no existe debe indicarlo

dictionary = {"perro":"dog","gato":"cat"}

def busClave (diccionario):
    clave = input("Ingrese la clave que desea buscar: ")
    valor1 = diccionario[clave]
    valor = type(valor1)
    if valor is str:
        valor = "cadena"
    else:
        valor = "Entero"
    if clave in diccionario:
        return f"La clave es {clave} su valor es {valor1} y el tipo de dato del valor es: {valor}"
    else:
        return f"No existe esa clave en el diccionario"
print(busClave(dictionary))
