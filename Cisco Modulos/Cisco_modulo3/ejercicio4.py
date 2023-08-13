# El ejercicio 4 constara de un codigo que permita que un usuario ingrese una contraseña por consola luego de haber
# echo esto, tendra que validarla nuevamente, si la contraseña no es valida tendra que volver a ingresarla hasta que 
# coinsida con la que ingreso la primera vez, esto se conseguira con el bucle whiley break 

# Se solicita por consola un string
contraseña1 = input("Escriba una contraseña: ")

# Se crea un bucle al cual se entrara ya que esta en True
while True :

    # Se solicita un nuevo string para compararlo con el anterior
    contraseña2 = input("Escriba su contraseña nuevamente: ")

    # Se realiza una validacion de la primera variable con la segunda, si esto es verdadero se parara el bucle, por la
    # palabra reservada break
    if contraseña1 == contraseña2:
        print("Su autenticacion fue todo un exito")
        break

    # Si la dicha validacion no es verdadera se mostrara un mensaje y seguira en dicho bucle
    else: 
        print ("Vuelva a ingresar su contraseña")
        
        