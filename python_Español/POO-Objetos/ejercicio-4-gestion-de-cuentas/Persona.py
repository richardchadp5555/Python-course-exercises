# Persona.py
# En este archivo creamos una clase Persona para guardar nombre, apellidos, DNI y edad de una persona
# Aplicamos encapsulamiento y tratamientos de errores.
# Se comprobará que el nombre, apelllidos no puedan ser cadenas vacías, además se comprobará que el DNI sea válido
# Autor: Richard Chadwick Plaza         Curso: 2ºDAM        Python

from validar_DNI import validarDni      # Función externa para validar el DNI

# Clase Persona
class Persona:
    def __init__(self, nombre = "", apellidos = "", dni = "", edad = 0):
        self.setNombre(nombre)
        self.setApellidos(apellidos)
        self.setDNI(dni)
        self.setEdad(edad)

    #   GETTERS
    def getNombre(self):
        return self.__nombre
    
    def getApellidos(self):
        return self.__apellidos
    
    def getDNI(self):
        return self.__dni
    
    def getEdad(self):
        return self.__edad
    
    # SETTERS
    def setNombre(self, nombreNuevo):
        if not nombreNuevo.strip():
            raise ValueError("Error: el nombre no puede ser un campo vacío. ")
        self.__nombre = nombreNuevo

    def setApellidos(self, apellidosNuevos):
        if not apellidosNuevos.strip():
            raise ValueError("Error: el campo de los apellidos no puede estar vacío. ")
        self.__apellidos = apellidosNuevos
    
    def setDNI(self, dniNuevo):
        if not validarDni(dniNuevo):
            raise ValueError("Error: el dni no es válido. ")
        self.__dni = dniNuevo

    def setEdad(self, edadNueva):
        if not isinstance(edadNueva, int) or edadNueva < 0:
            raise ValueError("La edad debe ser un número entero positivo. ")
        self.__edad = edadNueva

    # Método mayorDeEdad() que devuelve 'True' si la persona es mayor de edad o 'False' si no lo es
    def mayorDeEdad(self):
        return self.getEdad() >= 18
    
    # Método mostrar() que devuelve un string con la información de la persona
    def mostrar(self):
        return f"Nombre: {self.getNombre()}, Apellidos: {self.getApellidos()}, DNI: {self.getDNI()}, Edad: {self.getEdad()}"