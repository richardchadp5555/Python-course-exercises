# Electronico.py
# Clase que hereda de la clase Producto
# Richard Chadwick Plaza

from Producto import Producto

# Constante para controlar que no se aplique un descuento superior al válido en un producto Electronico
MAX_DESCUENTO = 10

class Electronico(Producto):
    def __init__(self, nombre= "", precio = 0.0, descuento = 0):
        # Compruebo que el descuento no supera el máximo establecido antes de llamar a la clase Padre
        if descuento > MAX_DESCUENTO:
            raise ValueError(f"Error: el descuento no puede ser superior a{MAX_DESCUENTO}% en productos electrónicos")
        # Llamo al cosntructor de la superclase
        super().__init__(nombre, precio, descuento)

    # Sobrescribo el setter del descuento para garantizar que no se supera el maximo establecido
    def setDescuento(self, descuentoNuevo):
        if descuentoNuevo > MAX_DESCUENTO:
            raise ValueError(f"Error: el descuento no puede ser superior a {MAX_DESCUENTO}% en productos electrónicos")
        super().setDescuento(descuentoNuevo)  # Llamo al setter de la clase base

            