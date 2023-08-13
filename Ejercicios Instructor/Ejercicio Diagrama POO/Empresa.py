from Cliente import *
from Productos import *

class Empresa(Cliente):
    def __init__(self,id,nombre,tipo,telefono,fax):
        super().__init__(id,nombre,tipo)
        self.__id = id
        self.__nombre = nombre
        self.__tipo = tipo
        self.__telefono = telefono
        self.__fax = fax
        
    def getDatosEmpresa (self):
        return f"El id de su empresa con nombre {self.__nombre} sera {self.__id}, ustes es de tipo {self.__tipo}, su telefono es {self.__telefono} y su fax es {self.__fax}"
    
    def setId (self,id):
        self.__id = id
        return f"Su id cambio a ser {self.__id}"
    
    def setNom (self,nombre):
        self.__nombre = nombre
        return f"Su nombre cambio a ser {self.__nombre}"
    
    def setTipo (self,tipo):
        self.__tipo = tipo
        return f"Su tipo cambio a ser {self.__tipo}"
    
    def setTel (self,telefono):
        self.__telefono = telefono 
        return f"Su telefono cambio a ser {self.__telefono}"
    
    def setFax (self,fax):
        self.__fax = fax
        return f"Su fax ahora va a ser {self.__fax}"

    def descuentoProducto (self,producto,precio):
        self.__precio = precio
        descuento = self.__precio * 0.02
        self.__precio = self.__precio - descuento
        return f"Por ser un cliente Empresa el producto \"{producto}\" te quedara en {self.__precio} "
