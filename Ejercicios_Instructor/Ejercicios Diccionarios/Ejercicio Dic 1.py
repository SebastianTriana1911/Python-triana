# Funcion Recibe un diccionario y una palabra que representa la clave (key), y nos retorna el valor 
# asociado y el tipo de dato de ese valor. Si no existe debe indicarlo

# Se crea un diccionario con claves en español y los valores en ingles
dictionary = {"perro":"dog","gato":"cat"}

# Se crea una funcion que se pase como parametro un diccionario
def busClave (diccionario):
    # Se solicita por teclado la clave que se quiera buscar
    clave = input("Ingrese la clave que desea buscar: ")
    # A la variable valor1 se le asigna el valor que contenga el diccionario con la clave 
    # Correspondiente que escribio el usuario por teclado
    valor1 = diccionario[clave]
    # A la variable valor se le asigna el tipo de dato que contenga el valor de la clave 
    # Que dicho usuario solicito
    valor = type(valor1)
    # Se valida si valor es in str, si es asi se le cambia el valor a la variable valor por
    # Una cadena de texto
    if valor is str:
        valor = "cadena"
    # Si la validacion es False la variable valor se cambia por una cadena de texto "Entero"
    else:
        valor = "Entero"
    # Se valida si la clave que solicito el usuario esta en el diccionario y si es asi la funcion
    # Retorna la clave que solicito mas su valor y el tipo de dato que es el valor
    if clave in diccionario:
        return f"La clave es {clave} su valor es {valor1} y el tipo de dato del valor es: {valor}"
    # Si la validacion es False retornara el mensaje que la clave no existe en el diccionario
    else:
        return f"No existe esa clave en el diccionario"
print(busClave(dictionary))
