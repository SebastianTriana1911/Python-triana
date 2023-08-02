class Persona:
    def __init__ (self,documento,puntMat,puntNaturales,puntSoc,puntIng):
        self.__documento = documento
        self.__puntMat = puntMat
        self.__puntNat = puntNaturales
        self.__puntSoc = puntSoc
        self.__puntIng = puntIng
        
    def Datos (self):
        return f"{self.__documento} {self.__puntMat} {self.__puntNat} {self.__puntSoc} {self.__puntIng}"
    
    def getDocumento (self):
        return {self.__documento}
    
    def getMatematicas (self):
        return {self.__puntMat}
    
    def getNaturales (self):
        return {self.__puntNat}
    
    def getSociales (self):
        return {self.__puntSoc}
    
    def getIngles (self):
        return {self.__puntSoc}