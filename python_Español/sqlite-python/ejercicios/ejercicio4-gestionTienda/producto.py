# producto.py
# Clase Producto, modela los productos de la tienda
# Autor: Richard Chadwick Plaza
# Curso: Segundo de DAM
# Lenguaje: Python

class Producto:
    def __init__(self, id, nombre, precio, stock):
        self.id = id
        self.nombre = nombre
        self.precio = precio
        self.stock = stock
    def __str__(self):
        return f"{self.nombre} (ID: {self.id}), Precio: {self.precio}, Stock: {self.stock}"