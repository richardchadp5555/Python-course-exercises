# Ropa.py
# Clase Ropa, es clase hija de la clase Producto
# Richard Chadwick Plaza            Python

from Producto import Producto

# Descuento maximo
MAX_DESCUENTO = 20

# Clase Ropa
class Ropa(Producto):
    def __init__(self, nombre = "", precio = 0.0, descuento = 0.0):
        if descuento > MAX_DESCUENTO:
            raise ValueError(f"Error: el descuento no puede superar {MAX_DESCUENTO}% en productos de ropa")
        super().__init__(nombre, precio, descuento)

    # Sobrescribimos el setter descuento para evitar que se supere el máximo establecido
    def setDescuento(self, descuentoNuevo):
        if descuentoNuevo > MAX_DESCUENTO:
            raise ValueError(f"Error: el descuento no puede superar {MAX_DESCUENTO}% en productos de ropa")
        # Llamamos al setter de la clase Padre
        super().setDescuento(descuentoNuevo)