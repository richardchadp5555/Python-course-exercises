# Comida.py
# Clase Comida, clase hija de la clase Producto
# Richard Chadwcik Plaza             Python

from Producto import Producto

# Máximo descuento para la comida = 0
MAX_DESCUENTO = 0

#  Clase Comida
class Comida(Producto):
    def __init__(self, nombre = "", precio = 0.0, descuento = 0):
        if descuento > MAX_DESCUENTO:
            raise ValueError("Error: los productos de comida no pueden tener descuento. ")
        super().__init__(nombre, precio, descuento)
    
    # Sobrescribimos el setter de la clase Padre
    def setDescuento(self, descuentoNuevo):
        if descuentoNuevo > MAX_DESCUENTO:
            raise ValueError("Error: los productos de comida no pueden tener descuento. ")
        # Llamo al setter de la clase padre
        super().setDescuento(descuentoNuevo)
