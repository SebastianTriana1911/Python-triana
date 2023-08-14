from Productos import *
class Cliente:
    def __init__(self,id,nombre,tipo):
        self.__id = id
        self.__nombre = nombre
        self.__tipo = tipo
        self.__productos = []
        
    def getDatosCliente (self):
        return f"Su id es: {self.__id},su nombre es {self.__nombre}, su tipo es {self.__tipo},"
    
    def setId (self,id):
        self.__id = id
        return f"Su id cambio a ser {self.__id}"
    
    def setNom (self,nombre):
        self.__nombre = nombre
        return f"Su nombre cambio a ser {self.__nombre}"
    
    def setTipo (self,tipo):
        self.__tipo = tipo
        return f"Su tipo cambio a ser {self.__tipo}"
    
    def agregarProducto (self,producto):
        self.__productos.append(producto)
        
    def componerProducto (self,id,nombre,tipo,descripcion,precio):
        producto = Producto(id,nombre,tipo,descripcion,precio)
        self.__productos.append(producto)     

    def getProductosList (self):
        return self.__productos
        

    
    
    