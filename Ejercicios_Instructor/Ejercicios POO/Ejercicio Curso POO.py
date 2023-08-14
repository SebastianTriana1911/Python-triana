class Curso():
    def __init__ (self):
        self.__curso = []
        
    def ingCurso (self,curso):
        self.__curso += [curso]
        
    def getCursos (self):
        return self.__curso
    
    def busCursos (self,curso):
        self.curso = curso
        for i in (self.__curso):
            if curso == i:
                return f"{curso} si esta en la lista"
        else:
            return f"{curso} no se encuentra en la lista"
        
    def elimCurso (self,curso):
        self.curso = curso
        for i in (self.__curso):
            if curso == i:
                self.__curso.remove(curso)
                return self.__curso
        else:
            return f"{curso} no se remueve de la lista por que no existe dicho curso"
        
    def modCurso (self,curso1,curso2):
        self.curso1 = curso1
        self.curso2 = curso2
        for i in range (len(self.__curso)):
            if curso1 == self.__curso[i]:
                self.__curso[i] = curso2
        return self.__curso
    
p = Curso()
p.ingCurso("primero")
p.ingCurso("segundo")
p.ingCurso("tercero")
p.ingCurso("cuarto")
p.ingCurso("quinto")
print (p.getCursos())
print(p.busCursos("primero"))
print(p.elimCurso("tercero"))
print (p.modCurso("segundo", "segundoo"))



