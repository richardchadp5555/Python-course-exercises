# ejercicio1-clasePunto.py
# En este primer ejercicio haremos una clase Punto. Un punto esta representado en el campo cartesiano por dos atributos, x e y, estos representan los valores de las coordenadas cartesianas

import math

# Clase Punto
class Punto:
    # Constructor
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    # Método para mostrar el punto
    def mostrar(self):
        return f"({self.x}, {self.y})"

    # Método para calcular la distancia entre este y otro punto
    def distanciaDosPuntos(self, otro):
        dx = self.x - otro.x
        dy = self.y - otro.y
        return math.sqrt(dx * dx + dy * dy)

    # Método para trasladar el punto
    def trasladar(self, dx, dy):
        self.x += dx
        self.y += dy

# Ejemplo de uso
punto1 = Punto(3, 4)
punto2 = Punto(0, 0)

print("Punto 1:", punto1.mostrar())
print("Punto 2:", punto2.mostrar())
print("Distancia entre los puntos:", punto1.distanciaDosPuntos(punto2))

# Trasladar punto1
punto1.trasladar(1, 1)
print("Punto 1 trasladado:", punto1.mostrar())
