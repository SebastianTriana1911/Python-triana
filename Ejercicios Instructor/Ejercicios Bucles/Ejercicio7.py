# Escriba un programa que pregunte una y otra vez si desea continuar con el programa, siempre que se conteste 
# exactamente sí (en minúsculas y con tilde).

val1 = "sí"
val2 = input("Desea continuar con el programa: ")
if val2 != val1:
        print("Termino el programa")
else:
    while val2 == val1:
        val2 = input("Seguro quiere continuar con el programa: ")
        if val2 == val1:
             continue
        else:
             print("Termino el programa")
             break