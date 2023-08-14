# El ejercicio 2 constara de un codigo donde el usuario pueda ingresar la hora, los minutos
# y los segundos actuales, el sistema le mostrara que horas son un segundo despues de la 
# hora que inserto 

hora = int(input("Ingrese la hora: "))
minutos = int(input("Ingrese los minutos: "))
segundos = int(input("Ingrese los segundos: "))

if hora == 24 and segundos == 59:
    hora = 0
elif hora < 24 and segundos == 59 and minutos == 59:
    hora = hora + 1
if minutos == 59 and segundos == 59:
    minutos = 1
elif minutos < 59 and segundos == 59:
    minutos = minutos + 1
if segundos == 59:
    segundos = 0
elif segundos < 59:
    segundos = segundos + 1

print (f"Son las {hora} horas con {minutos} minutos y {segundos} segundos: {hora}:{minutos}:{segundos}")


