from Cliente import *
class Producto:
    def __init__(self,id,nombre,tipo,descripcion,precio):
        self.__id = id
        self.__nombre = nombre
        self.__tipo = tipo
        self.__descripcion = descripcion
        self.__precio = precio
    
    def getProducto (self):
        return f"El id del producto {self.__nombre} es {self.__id}, su tipo es {self.__tipo} su descipcion es {self.__descripcion} y su precio es de {self.__precio}"