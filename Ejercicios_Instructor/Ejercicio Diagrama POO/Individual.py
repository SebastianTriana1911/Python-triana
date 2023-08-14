from Cliente import *
from Productos import *

class Individual(Cliente):
    def __init__(self,id,nombre,tipo,email,telefono):
        super().__init__(id,nombre,tipo,)
        self.__id = id
        self.__nombre = nombre
        self.__tipo = tipo
        self.__email = email
        self.__telefono = telefono
        
    def getDatosIndividual (self):
        return f"Señor {self.__nombre}, su id es {self.__id}, usted es de tipo {self.__tipo}, su correo es {self.__email}, y su numero de contacto {self.__telefono}" 
    
    def setId (self,id):
        self.__id = id
        return f"Su id cambio a ser {self.__id}"
    
    def setNom (self,nombre):
        self.__nombre = nombre
        return f"Su nombre cambio a ser {self.__nombre}"
    
    def setTipo (self,tipo):
        self.__tipo = tipo
        return f"Su tipo cambio a ser {self.__tipo}"
    
    def setEmail (self,email):
        self.__email = email
        return f"Usted cambio si email por {self.__email}"
    
    def setTel (self,telefono):
        self.__telefono = telefono
        return f"Su telefono es {self.__telefono}"

    def descuentoProducto (self,producto,precio):
        self.__precio = precio
        descuento = self.__precio * 0.035
        self.__precio = self.__precio - descuento
        return f"Por ser un cliente Individual el producto \"{producto}\" te quedara en {self.__precio} "