# Importacion de la clase abstracta ABC y el decorador @abstractmethod del modulo abc.
from abc import ABC, abstractmethod

# Importacion de la clase 'Producto' desde el modulo producto.
from producto import Producto


# Definicion de la subclase abstracta 'Tienda' de la clase abstracta ABC.
class Tienda(ABC):
    # Metodo abstracto para ingresar un producto a la tienda.
    @abstractmethod
    def ingresar_producto(self, nombre, precio, stock):
        pass

    # Metodo abstracto para listar los productos disponibles en la tienda.
    @abstractmethod
    def listar_productos(self):
        pass

    # Metodo abstracto para realizar una venta de producto en la tienda.
    @abstractmethod
    def realizar_venta(self, nombre_producto, cantidad):
        pass


# Definicion de la clase concreta 'TiendaRestaurante' de la clase abstracta 'Tienda'. (Ejemplo de 'herencia')
class TiendaRestaurante(Tienda):
    tipo = "Restaurante"

    # Constructor de la clase con parametros 'nombre' y 'costo_delivery'.
    def __init__(self, nombre, costo_delivery):
        # Inicialización de atributos privados 'nombre' y 'costo_delivery'.
        self.__nombre = nombre
        self.__costo_delivery = costo_delivery
        # Inicializacion del atributo privado productos como una lista vacia.
        self.__productos = []

    # Metodo para ingresar un producto al restaurante.
    def ingresar_producto(self, nombre, precio, stock):
        p = Producto(nombre, precio)
        # Filtrado de productos, correlación con los productos que ya estan ingresados en cada tienda
        encontrados = list(filter(lambda x: x == p, self.__productos))
        # Si no se encontraron productos iguales, se agrega el nuevo producto al final de la lista con 'append'
        if len(encontrados) == 0:
            self.__productos.append(p)

    # Método para listar los productos disponibles en el restaurante.
    def listar_productos(self):

        # Verificacion de si hay productos en la lista.
        if len(self.__productos):
            retorno = ""
            # Iteracion sobre los productos para formar la cadena de retorno.
            for p in self.__productos:
                retorno += f"NOMBRE: {p.nombre}\t" + f"PRECIO: ${p.precio}\n\n"
            return retorno
        else:
            return "No hay productos para esta tienda"

    # Metodo para realizar una venta en el restaurante (aún no implementado).
    def realizar_venta(self, nombre_producto, cantidad):
        pass


# Definición de la clase concreta TiendaFarmacia que hereda de la clase abstracta Tienda.
class TiendaFarmacia(Tienda):
    # Definición del atributo de clase tipo.
    tipo = "Farmacia"

    # Constructor de la clase con parámetros nombre y costo_delivery.
    def __init__(self, nombre, costo_delivery):
        # Inicialización de atributos privados nombre y costo_delivery.
        self.__nombre = nombre
        self.__costo_delivery = costo_delivery
        # Inicialización del atributo privado productos como una lista vacía.
        self.__productos = []

    # Método para ingresar un producto a la farmacia.
    def ingresar_producto(self, nombre, precio, stock):
        # sourcery skip: simplify-len-comparison, swap-if-else-branches, use-named-expression
        p = Producto(nombre, precio, stock)
        # Filtrado de productos iguales al producto a ingresar.
        encontrados = list(filter(lambda x: x == p, self.__productos))
        # Si no se encontraron productos iguales, se agrega el nuevo producto.
        if len(encontrados) == 0:
            self.__productos.append(p)
        else:
            # Si se encontró un producto igual, se actualiza su stock.
            indice = self.__productos.index(p)
            self.__productos[indice].stock = p + self.__productos[indice]

    # Método para listar los productos disponibles en la farmacia.
    def listar_productos(self):
        # sourcery skip: remove-unnecessary-else, swap-if-else-branches
        # Verificación de si hay productos en la lista.
        if len(self.__productos):
            retorno = ""
            # Iteracion sobre los productos para formar la cadena de retorno.
            for p in self.__productos:
                m = ""
                if p.precio > 15000:
                    m = " (Este producto aplica para delivery sin costo)"
                retorno += f"NOMBRE: {p.nombre}\t" + f"PRECIO: ${p.precio}{m}\t"
            return retorno
        else:
            return "No hay productos para esta tienda"

    # Metodo para realizar una venta en la farmacia (aún no implementado).
    def realizar_venta(self, nombre_producto, cantidad):
        pass


# Definicion de la clase concreta TiendaSupermercado que hereda de la clase abstracta Tienda.
class TiendaSupermercado(Tienda):
    # Definicion del atributo de clase tipo.
    tipo = "Supermercado"

    # Constructor de la clase con parametros nombre y costo_delivery.
    def __init__(self, nombre, costo_delivery):
        # Inicializacion de atributos privados nombre y costo_delivery.
        self.__nombre = nombre
        self.__costo_delivery = costo_delivery
        # Inicializacion del atributo privado productos como una lista vacia.
        self.__productos = []

    # Metodo para ingresar un producto al supermercado.
    def ingresar_producto(self, nombre, precio, stock):
        # sourcery skip: simplify-len-comparison, swap-if-else-branches, use-named-expression
        p = Producto(nombre, precio, stock)
        # Filtrado de productos iguales al producto a ingresar.
        encontrados = list(filter(lambda x: x == p, self.__productos))
        # Si no se encontraron productos iguales, se agrega el nuevo producto.
        if len(encontrados) == 0:
            self.__productos.append(p)
        else:
            # Si se encontro un producto igual, se actualiza su stock.
            indice = self.__productos.index(p)
            self.__productos[indice].stock = p + self.__productos[indice]

    # Metodo para listar los productos disponibles en el supermercado.
    def listar_productos(self):
        # sourcery skip: remove-unnecessary-else, swap-if-else-branches
        # Verificacion de si hay productos en la lista.
        if len(self.__productos):
            retorno = ""
            # Iteracion sobre los productos para formar la cadena de retorno.
            for p in self.__productos:
                m = ""
                if p.stock < 10:
                    m = " (Producto con stock bajo)"
                retorno += (
                    f"NOMBRE: {p.nombre}\t"
                    + f"PRECIO: ${p.precio}\t"
                    + f"STOCK: {p.stock}{m}"
                )
            return retorno
        else:
            return "No hay productos para esta tienda"
