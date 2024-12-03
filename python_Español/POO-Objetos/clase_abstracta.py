# claseAbstracta.py
# Ejemplo de cómo usar clases abstractas en Python.
# Autor: Richard Chadwick Plaza        Curso: 2ºDAM        Python

from abc import ABC, abstractmethod

class Forma(ABC):
    """
    Clase abstracta que representa una forma geométrica.
    """

    @abstractmethod
    def area(self):
        """
        Calcula el área de la forma.
        Este método debe ser implementado por las clases derivadas.
        """
        pass

    @abstractmethod
    def perimetro(self):
        """
        Calcula el perímetro de la forma.
        Este método debe ser implementado por las clases derivadas.
        """
        pass

    def descripcion(self):
        """
        Método no abstracto que devuelve una descripción genérica.
        Las clases derivadas pueden sobrescribirlo si es necesario.
        """
        return "Esto es una forma geométrica."

# Clases concretas que heredan de Forma

class Rectangulo(Forma):
    """
    Clase concreta que representa un rectángulo.
    """

    def __init__(self, ancho, alto):
        self.ancho = ancho
        self.alto = alto

    def area(self):
        return self.ancho * self.alto

    def perimetro(self):
        return 2 * (self.ancho + self.alto)

class Circulo(Forma):
    """
    Clase concreta que representa un círculo.
    """

    def __init__(self, radio):
        self.radio = radio

    def area(self):
        return 3.14159 * (self.radio ** 2)

    def perimetro(self):
        return 2 * 3.14159 * self.radio

# Ejemplo de uso

if __name__ == "__main__":
    # No se puede instanciar una clase abstracta
    # forma = Forma()  # Esto lanza un TypeError

    # Usamos las clases concretas
    rectangulo = Rectangulo(5, 10)
    print(f"Rectángulo - Área: {rectangulo.area()}, Perímetro: {rectangulo.perimetro()}")

    circulo = Circulo(7)
    print(f"Círculo - Área: {circulo.area()}, Perímetro: {circulo.perimetro()}")

    print(circulo.descripcion())  # Método no abstracto heredado de Forma
