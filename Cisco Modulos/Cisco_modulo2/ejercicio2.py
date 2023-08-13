# El ejercicio numero 2 constara de un codigo donde se pueda insertar comillas dobles dentro de la funcion print() 
# con el caracter de escape " \ " 

a = input("Cual es tu nombre: ")
b = input("Cual es tu color favorito: ")
c = int(input("Cuantos annios tienes: "))

# Para poder insertar comillas dobles dentro de la funcion print() es necesario insertar el caracter de escape antes
# de la primera comilla, se digita la palabra que se desea y luego que inserta el caracter de escape seguido de la 
# segunda comilla asi: \"palabra\" y se veria asi en consola: "palabra".

print ("Tu \"nombre\" es", a + " tu \"color\" favorito es el", b + " y tienes", c ,"\"annios\".")