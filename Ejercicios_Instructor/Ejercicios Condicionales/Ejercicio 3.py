# El ejercicio 3 constara de un codigo donde se determine el mayor de 3 numero ingresados
# por el usuario con la funcion if - elif - else

x=int(input('ingrese numero: '))
y=int(input('ingrese numero: '))
z=int(input('ingrese numero: '))

#indentación

if x>y:
    if x>z:
        print(f'el mayor es {x}')
    else:
        print(f'el mayor es {z}')
else:
    if y>z:
        print(f'el mayor es {y}')
    else:
        print(f'el mayor es {z}')