
# Programación Orientada a Objetos en Python

En este directorio tendremos ejercicios varios para aprender y practicar los conceptos fundamentales de la **Programación Orientada a Objetos (POO)** en Python. La POO es un paradigma de programación basado en la creación y manipulación de "objetos" que modelan elementos del mundo real o abstracto.

## Ejercicios:
- **ejercicio1-clasePunto.py**: primer ejercicio de POO donde trabajamos con una clase sencilla que representa un Punto en el eje cartesiano, sus atributos son las coordenadas x e y. Además, implementamos un método para calcular la distancia entre dos puntos y otro para trasladar un punto una distancia determinada
- **ejercicio2-claseAlumno.py**: en este ejercicio practicamos con el encapsulamiento en Python. Creamos una clase Alumno que tiene un atributo privado y demostramos como es necesario el empleo de métodos getters y setters para acceder a él y cambiar su valor

## Conceptos Esenciales

### 1. **Clases y Objetos**
- **Clase**: Es un molde o plantilla para crear objetos. Define atributos (propiedades) y métodos (funciones asociadas a la clase).
- **Objeto**: Es una instancia de una clase, es decir, una realización concreta de la plantilla definida por la clase.

#### Ejemplo:
```python
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    def saludar(self):
        print(f"Hola, soy {self.nombre} y tengo {self.edad} años.")

# Crear un objeto
persona1 = Persona("Carlos", 25)
persona1.saludar()
```

---

### 2. **Atributos**
- **Atributos de instancia**: Variables que pertenecen a una instancia concreta de una clase.
- **Atributos de clase**: Variables que son compartidas por todas las instancias de la clase.

#### Ejemplo:
```python
class Circulo:
    # Atributo de clase
    pi = 3.14159

    def __init__(self, radio):
        self.radio = radio  # Atributo de instancia

    def calcular_area(self):
        return Circulo.pi * (self.radio ** 2)

circulo1 = Circulo(5)
print(circulo1.calcular_area())
```

---

### 3. **Métodos**
- Son funciones definidas dentro de una clase que operan sobre sus objetos.
- **Métodos de Instancia**: Trabajan con atributos de instancia.
- **Métodos de Clase**: Usan `@classmethod` y trabajan con atributos de clase.
- **Métodos Estáticos**: Usan `@staticmethod` y no dependen de la clase ni de las instancias.

#### Ejemplo:
```python
class Calculadora:
    @staticmethod
    def sumar(a, b):
        return a + b

print(Calculadora.sumar(10, 20))
```

---

### 4. **Herencia**
- Permite que una clase (clase hija) herede atributos y métodos de otra clase (clase padre).

#### Ejemplo:
```python
class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

    def hablar(self):
        pass

class Perro(Animal):
    def hablar(self):
        return "Guau!"

class Gato(Animal):
    def hablar(self):
        return "Miau!"

perro = Perro("Rex")
gato = Gato("Pelusa")
print(perro.hablar())
print(gato.hablar())
```

---

### 5. **Polimorfismo**
- La capacidad de diferentes clases de responder a los mismos métodos, incluso si su implementación es distinta.

#### Ejemplo:
```python
def hacer_hablar(animal):
    print(animal.hablar())

hacer_hablar(perro)  # Salida: "Guau!"
hacer_hablar(gato)   # Salida: "Miau!"
```

---

### 6. **Encapsulamiento**
- Restringe el acceso directo a los atributos y métodos de un objeto para protegerlos. En Python:
  - Los atributos con `_` son protegidos (convención).
  - Los atributos con `__` son privados.

#### Ejemplo:
```python
class CuentaBancaria:
    def __init__(self, saldo):
        self.__saldo = saldo  # Atributo privado

    def depositar(self, cantidad):
        self.__saldo += cantidad

    def obtener_saldo(self):
        return self.__saldo

cuenta = CuentaBancaria(100)
cuenta.depositar(50)
print(cuenta.obtener_saldo())
```

---

### 7. **Abstracción**
- Permite definir métodos en clases base que deben ser implementados en las clases hijas.

#### Ejemplo:
```python
from abc import ABC, abstractmethod

class Figura(ABC):
    @abstractmethod
    def calcular_area(self):
        pass

class Rectangulo(Figura):
    def __init__(self, ancho, alto):
        self.ancho = ancho
        self.alto = alto

    def calcular_area(self):
        return self.ancho * self.alto

rectangulo = Rectangulo(10, 5)
print(rectangulo.calcular_area())
```
---
## Ejercicios:

### 1. **Clase Punto**
Archivo: `ejercicio1-clasePunto.py`

- Representa un punto en un plano cartesiano mediante dos atributos (`x` y `y`).
- Implementa métodos para calcular la distancia entre dos puntos y para trasladar un punto.

### 2. **Clase Alumno**
Archivo: `ejercicio2-claseAlumno.py`

- Practica el encapsulamiento en Python.
- Define un atributo privado (`__atributoPrivado`) y su acceso a través de getters y setters.

### 3. **Diccionario de Contactos**
Carpeta: `ejercicio-3-diccionario-de-contactos`

Este proyecto incluye:
- **`Persona.py`:** Clase que encapsula datos como nombre, dirección y teléfono con validaciones.
- **`Principal.py`:** Programa principal que implementa un diccionario de contactos con opciones para añadir, modificar, buscar, listar y eliminar contactos.

#### Funcionalidades:
- Listado de contactos ordenado alfabéticamente.
- Gestión de contactos con validaciones en nombre y teléfono.

### 4. **Gestión de Cuentas Bancarias**
Carpeta: `ejercicio-4-gestion-de-cuentas`

Este proyecto incluye:
- **`Persona.py`:** Clase que encapsula información personal (nombre, apellidos, DNI y edad).
- **`Cuenta.py`:** Clase para gestionar una cuenta bancaria con operaciones básicas.
- **`CuentaJoven.py`:** Subclase de `Cuenta`, destinada a titulares menores de 25 años con bonificación.
- **`validar_DNI.py`:** Función para validar el formato del DNI.
- **`Principal.py`:** Programa principal para gestionar cuentas, incluyendo un menú interactivo.

#### Funcionalidades:
- Crear cuentas normales y cuentas jóvenes.
- Ingresar, retirar y listar cuentas.
- Validación de DNI y restricciones para cuentas jóvenes.

### 5. **Gestión de Productos**
Carpeta: `ejercicio-5-gestion-productos`

Este proyecto incluye:
- **`Producto.py`:** Clase base para representar un producto con atributos como nombre, precio y descuento.
- **`Comida.py`:** Subclase que representa productos alimenticios, sin permitir descuentos.
- **`Electronico.py`:** Subclase para productos electrónicos, con un descuento máximo del 10%.
- **`Ropa.py`:** Subclase para productos de ropa, con un descuento máximo del 20%.
- **`Principal.py`:** Programa principal para gestionar productos mediante un menú interactivo.

#### Funcionalidades:
- Añadir productos (electrónicos, ropa, comida).
- Calcular precio final tras aplicar descuentos.
- Listar todos los productos registrados.

---

## Requisitos
- **Python 3.8 o superior**.
- Un editor de código como **Visual Studio Code** o **PyCharm**.

---

**Autor:** Richard Chadwick Plaza  
**Curso:** Segundo de DAM  
**Asignatura:** Python
