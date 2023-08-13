# El ejercio numero 3 constara de un comentario mostrado por consola donde se muestre por cada espacio de una
# palabra un caracter especifico con el argumento sep=(), veremos como se utiliza y que hace la funcion \n y por
# ultimo en la linea de codigo 16 veremos en funcionamiento el argumento end=().


# El argumento sep() nos servira para colocar en el espacio de una a otra cadena de texto el simbolo o letra que 
# nosotros queramos 
print("Hola", "mi nombre es Sebastian \n", sep=",")

# La funcion \n permitira hacer un salto de linea ejecutando lo que le siga en una siguiente linea mostandolo en la 
# consola, para que funcione debe estar dentro de la cadena de texto
print("El dia que se esta haciendo este codigo es 23", "04", "2023 \n", sep="-")
print("Gracias", " Por su atencion", "\n", sep=".")

# El argumento end() nos servira para colocar un simbolo y una letra a lo ultimo de cada cadena de texto
print("Recuerde que acaba de ver el ejercicio numero 3", end=".")
