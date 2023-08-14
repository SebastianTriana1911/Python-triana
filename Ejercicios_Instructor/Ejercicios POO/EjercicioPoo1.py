class Persona():
    def __init__(self,nombre,documento):
        self.__nombre = nombre
        self.__documento = documento
        self.__curso = []
    
    def getnombre (self):
        return self.__nombre
    
    def getdocumento(self):
        return self.__documento
    
    def setnombre(self,nombre):
        self.__nombre = nombre
    
    def setdocumento(self,documento):
        self.__documento = documento
        
    def mostrarDatos (self):
        return f"{self.__nombre} {self.__documento}"
    
    def agregarCurso (self,curso):
        self.__curso += [curso]
        
    def getcurso (self):
        return self.__curso

p = Persona("Sebas",19)
q = Persona("David", 20)

print(p.getnombre(), p.getdocumento(),)
print (p.getnombre())
print(p.getdocumento())
p.setnombre("Andres")
print(p.getnombre())
print(p.mostrarDatos())
print(p.agregarCurso("primero"))
print(p.getcurso())


