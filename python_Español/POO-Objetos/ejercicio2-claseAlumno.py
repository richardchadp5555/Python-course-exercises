# ejercicio2-claseAlumno.py
# En esta clase practicamos con el concepto del encapsulamiento en la programación orientada a objetos. El encapsulamiento es una característica que consiste en restringir el acceso directo a los atributos de una clase. En lugar de acceder directamente a los atributos, se utilizan métodos (getters y setters) para leer o modificar esos valores. Esto mejora la seguridad y la integridad de los datos del programa.
# En python los atributos privados se definen mediante el uso de un doble guion bajo (__). Esto no significa que los atributos sean completamente inaccesibles, sino que Python aplica una técnica llamada name mangling (manipulación de nombres). Esto renombra internamente el atributo, añadiendo un prefijo con el nombre de la clase, para evitar que se acceda fácilmente desde fuera.

class Alumno():
    def __init__(self, nombre = ""):
        self.nombre = nombre
        self.__atributoPrivado = "hola"
    
    # Para acceder al atributoPrivado necesitamos un método getter
    def getAtributoPrivado(self):
        return self.__atributoPrivado
    
    # Para cambiar su valor necesitamos un setter
    def setAtributoPrivado(self, nuevoAtributoSecreto):
        self.__atributoPrivado = nuevoAtributoSecreto

alumno1 = Alumno("jose")
# print(alumno1.__atributoPrivado)    # Esto da un error por que es un atributo privado

print( "El atributo privado es ", alumno1.getAtributoPrivado())
alumno1.setAtributoPrivado("adios")
print("El atributo privado ha cambiado ahora es: ", alumno1.getAtributoPrivado())