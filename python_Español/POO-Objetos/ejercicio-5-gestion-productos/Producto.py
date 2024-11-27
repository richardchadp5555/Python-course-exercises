# Producto.py
# Richard Chadwick Plaza

class Producto():
    def __init__(self, nombre = "", precio = 0.0, descuento = 0):
        self.setNombre(nombre)
        self.setPrecio(precio)
        self.setDescuento(descuento)

    # Getters
    def getNombre(self):
        return self.__nombre
    
    def getPrecio(self):
        return self.__precio
    
    def getDescuento(self):
        return self.__descuento
    
    # Setters
    def setNombre(self, nombreNuevo):
        if not nombreNuevo.strip():
            raise ValueError("Error: el nombre no puede ser un campo vacío. ")
        self.__nombre = nombreNuevo

    def setPrecio(self, precioNuevo):
        if not isinstance(precioNuevo, (float, int)) or precioNuevo < 0:
            raise ValueError("Error el precio debe ser un número positivo")
        self.__precio = precioNuevo
    
    def setDescuento(self, descuentoNuevo):
        if not isinstance(descuentoNuevo, int) or  not (0 <= descuentoNuevo <= 100):
            raise ValueError("Error el descuento es un porcentaje, su valor debe estar entre 0 y 100 ")
        self.__descuento = descuentoNuevo

    # Método para calcular el precio final después del descuento
    def calcularPrecioFinal(self):
        return self.__precio * (1 - self.__descuento / 100)
    

    # Método para mostrar el objeto y sus atributos
    def __str__(self):
        return f"Producto: [Nombre] = {self.getNombre()}, [Precio]: {self.getPrecio()}, [Descuento]: {self.getDescuento()}"