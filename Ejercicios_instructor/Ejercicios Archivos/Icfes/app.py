from persona import *
import csv

personas = []
with open ("C:\\Users\\Sebastian\\OneDrive\\Escritorio\\Clone\\pythontriana\\Ejercicios_instructor\\Ejercicios Archivos\\Saber_11.csv", encoding= "utf-8" ) as archivo:
    saber = csv.reader (archivo)
    for row in saber:
        persona1 = Persona(row[0], row[2], row[10], row[14])
        personas.append(persona1)

# Hallar la moda de la lista documentos
def modaDocumento ():
    documentos = []
    diccionario = {}

    for lista in personas:
        for documento in lista.getDocumento():
            if documento == "ESTU_TIPODOCUMENTO":
                continue
            if documento == "TI":
                documentos.append(1)
            elif documento == "CC":
                documentos.append(2)
            elif documento == "PEP":
                documentos.append(3)
            elif documento == "CE":
                documentos.append(4)
            elif documento == "NES":
                documentos.append(5)
            elif documento == "PE":
                documentos.append(6)
            elif documento == "CR":
                documentos.append(7)
            for numero in documentos:
                clave = str(numero)
                if clave not in diccionario:
                    diccionario [clave] = 1
                else:
                    diccionario [clave] += 1 
    frecuencia = 0
    moda = documentos[0] 
    for num in diccionario:
        if diccionario[num] > frecuencia:
            moda = num
            frecuencia = diccionario[num]
    if moda == "1":
        moda = "TI"
    if moda == "2":
        moda = "CC"
    if moda == "3":
        moda = "PEP"
    if moda == "4":
        moda = "CE"
    if moda == "5":
        moda = "NES"
    if moda == "6":
        moda = "PE"
    return f"El documento que mas se repite en las pruebas saber 11 fue: {moda}"

# Hayar la moda entre los generos 
def modaGenero ():
    generos = []
    diccionario = {}

    for lista in personas:
        for sexo in lista.getSexo():
            if sexo == "ESTU_GENERO":
                continue
            if sexo == "M":
                generos.append(1)
            elif sexo == "F":
                generos.append(2)        
            for s in generos:
                clave = str(s)
                if clave not in diccionario:
                    diccionario [clave] = 1
                else:
                    diccionario [clave] += 1 
    frecuencia = 0
    moda = generos[0] 
    for num in diccionario:
        if diccionario[num] > frecuencia:
            moda = num
            frecuencia = diccionario[num]
    if moda == "1":
        moda = "MASCULINO (M)"
    if moda == "2":
        moda = "FEMENINO (F)"
    return f"En la prueba Saber 11 predomino el sexo {moda}"

# Hayar moda de los departamentos
def departamentos ():
    departamentos = []
    diccionario = {}
    for i in personas:
        for depa in i.getEtnia():
            if depa == "ESTU_DEPO_RESIDE":
                    continue
            if depa == "MAGDALENA":
                departamentos.append(1)
            elif depa == "BOGOTA":
                departamentos.append(2)        
            elif depa == "BOLIVAR":
                departamentos.append(3)
            elif depa == "ATLANTICO":
                departamentos.append(4)
            elif depa == "VALLE":
                departamentos.append(5)
            elif depa == "SANTANDER":
                departamentos.append(6)
            elif depa == "CUNDINAMARCA":
                departamentos.append(7)
            elif depa == "SUCRE":
                departamentos.append(8)
            elif depa == "BOYACA":
                departamentos.append(9)
            elif depa == "ANTIOQUIA":
                departamentos.append(10)
            elif depa == "CESAR":
                departamentos.append(11)
            elif depa == "HUILA":
                departamentos.append(12)
            elif depa == "CASANARE":
                departamentos.append(13)
            elif depa == "CAUCA":
                departamentos.append(14)
            elif depa == "CORDOBA":
                departamentos.append(15)
            elif depa == "NORTE SANTANDER":
                departamentos.append(16)
            elif depa == "QUINDIO":
                departamentos.append(17)
            elif depa == "ARAUCA":
                departamentos.append(18)
            elif depa == "META":
                departamentos.append(19)
            for s in departamentos:
                clave = str(s)
                if clave not in diccionario:
                    diccionario [clave] = 1
                else:
                    diccionario [clave] += 1 
    frecuencia = 0
    moda = departamentos[0] 
    for num in diccionario:
        if diccionario[num] > frecuencia:
            moda = num
            frecuencia = diccionario[num]
    if moda == "1":
        moda = "MAGDALENA"
    if moda == "2":
        moda = "BOGOTA"
    if moda == "3":
        moda = "BOLIVAR"
    if moda == "4":
        moda = "ATLANTICO"    
    return f"El departamento con mas estudiantes de la prueba Saber 11 fue {moda}"



# Promedio de estratos
def promEstrat():
    estratos = []
    for estrato in personas:
        for numero in estrato.getEstrato():
            if numero == " 1":
                estratos.append (1)
            elif numero == " 2":
                estratos.append (2)
            elif numero == " 3":
                estratos.append (3)
            elif numero == " 4":
                estratos.append (4)
            elif numero == " 5":
                estratos.append (5)
            else:
                continue
    suma = 0
    for sum in estratos:
        suma = suma + sum

    elementos = 0
    for i in range (len(estratos)):
        elementos = elementos + 1

    promedio = suma // elementos
    return f"El promedio de personas que presentaron la prueba a Saber 11 son de estrato {promedio}"

with open ("C:\\Users\\Sebastian\\OneDrive\\Escritorio\\Clone\\pythontriana\\Ejercicios_instructor\\Ejercicios Archivos\\respuestaIcfes.txt", "w", encoding= "utf-8") as archivo:
    res1 = modaDocumento()
    archivo.write(f"{res1}\n")
    res2 = modaGenero()
    archivo.write(f"{res2}\n")
    res3 = departamentos()
    archivo.write(f"{res3}\n")
    res4 = promEstrat()
    archivo.write(f"{res4}\n")
