# Persona.py
# En este archivo creamos una clase Persona para guardar nombre, dirección, y teléfono de una persona. 
# Aplicamos encapsulamiento y tratamientos de errores.
# Se comprobará que el teléfono no sea un campo vacío y cumpla con un formato adecuado de 9 dígitos, un teléfono válido podría ser 123456789
# Se comprobará que el nombre del contacto no sea un campo vacío
# Autor: Richard Chadwick Plaza         Curso: 2ºDAM        Python


import re # Módulo para expresiones regulares

# Clase Persona
class Persona(): 
    # Constructor
    def __init__(self, nombre = "", direccion = "", telefono = ""):
      self.__nombre = self.__validarNombre(nombre)
      self.__direccion = direccion                      # La dirección podria ser un campo vacío
      self.__telefono = self.__validarTelefono(telefono)
        
    # Métodos getters
    def getNombre(self):
      return self.__nombre
     
    def getDireccion(self):
        return self.__direccion
     
    def getTelefono(self):
        return self.__telefono
     
     # Métodos setters
    def setNombre(self, nuevoNombre):
        self.__nombre = self.__validarNombre(nuevoNombre)

    def setDireccion(self, nuevaDireccion):
        self.__direccion = nuevaDireccion
    
    def setTelefono(self, nuevoTelefono):
        self.__telefono = self.__validarTelefono(nuevoTelefono)

    # Método para validar teléfonos, devuelve el teléfono si es correcto
    def __validarTelefono(self, telefono):
        patronTelefonoValido = r"^\d{9}$"
        if not re.fullmatch(patronTelefonoValido, telefono):
            raise ValueError("Error: el teléfono proporcionado no cumple con el formato válido de 9 dígitos.")
        return telefono
    
    # Metodo para validar el nombre, devuelve el nombre si es correcto
    def __validarNombre(self, nombre):
        if not nombre.strip():
            raise ValueError("Error: el nombre no puede ser un campo vacío")
        return nombre
    
    # Método que devuelve un string con la información de la persona
    def __str__(self):
        return f"Nombre: {self.__nombre}, Dirección: {self.__direccion}, Teléfono: {self.__telefono}"