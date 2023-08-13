# El ejercicio 2 constara de ingresar un dia de la semana, segun el dia la consola mostrara con que instructor
# del Sena le tocara ese respectivo dia, este ejercicio se hara con la sentencia if - elif - else

# Se solicita por parametro un dia de la semana para guardarlo en la variable dia
dia = input("Escriba un dia de la semana: ")

# Si el dia es alguno de los dias de la semana mostrara el mensaje correspondiente si el dia de la semana no 
# Existe o esta escriba de otra manera se le mostrara un mensaje que ingreso lo que no era
if dia == "lunes":
    print("\nHoy toca clase con el profesor Samuel")

elif dia == "martes":
    print("\nHoy toca clase con el profesor Evelio")

elif dia == "miercoles":
    print("\nHoy toca con el profesor Samuel")

elif dia == "jueves":
    print("\nHoy toca clase con el profesor Evelio")

elif dia == "viernes":
    print("\nHoy toca clase con el profesor Samuel")

elif dia == "sabado":
    print("\nHoy toca descansar de los profesores")

elif dia == "domingo":
    print("\nHoy toca descansar de los profesores")

else:
    print("\nIngresaste el dia de la semana mal o simplemente no es un dia")