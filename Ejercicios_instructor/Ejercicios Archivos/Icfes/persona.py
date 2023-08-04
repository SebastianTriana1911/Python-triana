class Persona:
    def __init__ (self,documento,sexo,etnia,estrato):
        self.__documento = documento
        self.__sexo = sexo
        self.__etnia = etnia
        self.__estrato = estrato
        
    def Datos (self):
        return f"{self.__documento} {self.__sexo} {self.__etnia} {self.__estrato}"
    
    def getDocumento (self):
        return {self.__documento}
    
    def getSexo (self):
        return {self.__sexo}
    
    def getEtnia (self):
        return {self.__etnia}
    
    def getEstrato (self):
        return {self.__estrato}