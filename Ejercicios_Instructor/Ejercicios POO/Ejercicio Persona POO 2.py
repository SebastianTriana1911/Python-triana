class Personas:
    cursos = []
    def __init__ (self,nombre,edad):
        self.__nombre = nombre
        self.__edad = edad
        self.__curso = []
        
    def getDatos (self):
        return f"{self.__nombre} {self.__edad} {self.__curso}"
        
    def setCurso (self, curso):
        self.curso = curso
        self.__curso.append(curso)
        for i in self.__curso:
            if i not in Personas.cursos:
                Personas.cursos.append (i)

p = Personas("Peter", 18)
print (p.setCurso("Python"))
print (p.getDatos())

q = Personas ("Capera", 17)
print (q.setCurso("CSS"))
print (q.getDatos())

a = Personas("Peña", 19)
print (a.setCurso("Java"))

print(Personas.cursos)
