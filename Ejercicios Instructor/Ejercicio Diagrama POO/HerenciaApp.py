from Cliente import *
from Productos import *
from Individual import *
from Empresa import *

# Se instancian objetos de la clase Cliente
persona = Cliente(1,"persona","cliente general")
persona2 = Cliente(2,"persona2","cliente general")

# Al objeto persona se le añade los metodos getDatos para visualizar todos los datos y el setId para modificar el Id
print (persona.getDatosCliente())
print (persona.setId(11))
print (persona.setNom("Personas"))
print (persona.getDatosCliente())
print ()

"""-------------------------------------------AGREGACION ---------------------------------------------------------"""

# Se instancian 2 objetos ob1 y ob2 de la clase Producto 
ob1 = Producto(1,"Arroz","Grano","Grasas",1000)
ob2 = Producto(2,"Lenteja","Grano","Engorda",2000)

# A los dos objetos previamente instanciados se le asignan el metodo getProducto que viene de la clase Producto, estos 
# dos prints nos retornaran el valor de cada uno de los objetos
print(ob1.getProducto())
print(ob2.getProducto())
print ()

# Al objeto persona instanciado de la clase Cliente se le agrega el metodo agregarProducto con el parametro de 
# un producto, en este caso le pasaremos el objeto ob1 y ob2 creado desde la clase Producto para que lo añada en la lista de 
# productos del objeto al que se le esta pasando el metodo, lo que sucedera va a ser que se va añadir ob1 y ob2 a la 
# lista producto como ya lo habiamos dicho y nos mostrara es la direccion de memoria ya que por el momento ob1 y ob2 son 
# simplemente dos objetos
persona.agregarProducto(ob1)
persona.agregarProducto(ob2)

# Creamos un bucle for con una variable llamada productos que nos recorra la lista de productos que tiene el objeto persona
# llamando al objeto seguido del metodo getProductos que es el metodo que nos permite visualizar la lista de dichos productos
for producto in persona.getProductosList():
    # Por cada vuelta que haga la variable producto la imprimiremos llamando dicha variable con el metodo getProducto, que nos
    # permitira visualizar cada uno de los productos que contiene la lista getProducto del objeto persona
    print (f"AGREGACION: {producto.getProducto()}")
print ()

"""-------------------------------------------COMPOSICION-------------------------------------------------------------------"""

# En la linea 7 previamente ya habiamos instanciado el objeto persona2 con la clase Cliente a hora le vamos añaridir productos
# a dicho objeto con el metodo componerProducto y sus parametros, a la hora de llamar este metodo nos va a permitir llenar la
# lista con los diferentes parametros que le hayamos pasado como si fuera un objeto, la diferencia es que como dicho objeto ya
# esta incorporado en el objeto persona2, a la hora de eliminar este objeto se eliminara la lista con la informacion que le 
# hayamos pasado como producto, esta es la diferencia de la composicion y la agregacios y de los metodos agragarProducto y 
# componerProducto
persona2.componerProducto(2,"Arroz","Grano","Grasas",2000)
persona2.componerProducto(3,"Arroz","Grano","Grasas",2000)
for producto in persona2.getProductosList():
    print (f"COMPOSICION {producto.getProducto()}")
print()

# Se crea una instancia de la clase Individual, llamada persona3, donde se le pasan los parametros establecidos para esa clase 
persona3 = Individual (20,"persona3","Individual","sebas@gmail.com", 313802)

# Ahora desearemos ver los datos de dicho objeto y lo haremos con el metodo que ya tiene previamente la clase con la que se a instanciado
# el objeto en cual es el metodo getDatosIndividual. Podriamos usar el metodo getDatosClientes pero este solo nos mostrara los datos que 
# se necesitan al instanciar un objeto de esa clase mas no de la clase Individual que es en la que estamos trabajando ahorita
print(persona3.getDatosIndividual())

# Al objeto persona3 le deseamos cambiar en nombre por personita3 dicha clase con la que esta instanciado el objeto tiene un metodo el cual
# nos permite hacer esto y se llama setNom 
# NOTA: Hay un metodo que nos permite hacer esto en la clase Cliente pero a la hora visualizar los datos del objeto instanciado de la clase
# Individual no mostrara los cambios ya que el metodo no es propio de la clase, por esta razon usamos los metodos que le hemos puesto a la 
# clase en la que hemos instanciado el objeto
print(persona3.setNom("personita3"))
print(persona3.getDatosIndividual())
print ()

# Al objeto persona3 le asignamos el metododo componerProducto que se encuentra en la superClass Cliente, como ya vimos este metodo nos 
# permite hacer una relacion de composicion entre los productos que es en este caso y el objeto persona3, al metodo le asignamos como 
# parametro el id, el nombre, el tipo, la descripcion y el precio, para añadirlo a la lista de productos que se asigno en la superClass
persona3.componerProducto(30,"Manzana","Fruta","...",1500)

# Creamos una for con una variable como nombre producto que nos recorra la lista de productos que contiene el objeto persona3, esto hace 
# que la variable producto se convierta el cada uno de los objetos que se indexan a la lista productos gracias al metodo componerProducto
for producto in persona3.getProductosList():
    # Imprimiremos la variable producto, "si imprimimos solo la variable nos imprimira la posicion de memoria, ya que producto va a ser un"
    # objeto" por eso para visualizar el objeto que sea la variable producto usaremos el metodo getProducto que nos permite ver dicho objeto
    print(producto.getProducto())

# Como los objetos instanciados de la clase Individual tienen un descuento del 3.5% en cualquier producto, se creo un metodo en dicha clase
# que nos permitiera sacar el descuento de algun producto pasandole como parametro el nombre del producto y el precio de ese producto, y ese
# metodo fue descuentoProducto. Como persona3 es una persona Individual ya que esta instanciada de dicha clase podra utilizar dicho metodo
# y aplicar dicho descuento en su producto
print(persona3.descuentoProducto("Manzana",1500))
print ()

"""---------------------------------------------------------------------------------------------------------------------------------------"""
# De esa linea de codigo para abajo podremos ver lo mismo anteriormente explicado solo que en la ultima linea de codigo vemos como usamos
# un metod llamado descuentoProducto que este es propio de la clase Empresa que es la clase en la que hemos instanciado el objeto sena, 
# este metodo nos permite saber el descuento que se establecen a los productos que adquieren las empresas y funciona igual que el metodo
# descuentoProducto de la clase Individual solo que ese metodo establece un descuento del 3.5% y este un descuento del 2% por producto
sena = Empresa(10,"Sena","Empresa",312421,"sena@gmail.com")
print (sena.getDatosEmpresa())
print ()

sena.componerProducto(10,"Computador","Electronico","...",1500000)
for producto in sena.getProductosList():
    print(producto.getProducto())
print(sena.descuentoProducto("Ctadompuor",1500000))




