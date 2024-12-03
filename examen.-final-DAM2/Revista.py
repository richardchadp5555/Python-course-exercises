# Libro.py
# Clase Libro que hereda de la clase Material
# Richard Chadwick Plaza

from Material import Material

# Lista de meses
meses = ["enero", "febrero", "marzo", "abril", "mayo", "junio", "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"]

def mesesValidos():
    return meses

mesPorDefecto = "enero"

class Revista(Material):
    def __init__(self, id = 0, titulo = "", autor = "Anónimo", anioPublicacion = 0000, numEdicion = 0, mesPublicacion = mesPorDefecto):
        # Controlamos que el genero esta en la lista
        if mesPublicacion.strip().lower() not in meses:
            raise ValueError("Error: el mes de publicación de la revista tiene que ser un mes del año real. ")
        mesPublicacion.strip().lower()
        self.setMesPublicacion(mesPublicacion)

        # Controlamos que el número de edición sea un entero positivo
        if not isinstance(numEdicion, int) or numEdicion < 0:
            raise ValueError("Error el número de edición debe ser un número entero positivo")
        self.setNumEdicion(numEdicion)

        # Inicializamos los atributos de la clase Padre
        super().__init__(id, titulo, autor, anioPublicacion)

    # Getters
    def getMesPublicacion(self):
        return self.__mesPublicacion
        
    def getNumEdicion(self):
        return self.__numEdicion
        
    # Setters
    def setMesPublicacion(self, mesPublicacionNuevo):
        if mesPublicacionNuevo.strip().lower() not in meses:
            raise ValueError("Error: el mes de publicación de la revista tiene que ser un mes del año real. ")
        self.__mesPublicacion = mesPublicacionNuevo.strip().lower()

    def setNumEdicion(self, numEdicionNuevo):
        if not isinstance(numEdicionNuevo, int) or numEdicionNuevo < 0:
            raise ValueError("Error el número de edición debe ser un número entero positivo")
        self.__numEdicion = numEdicionNuevo

    # Sobrescribimos el mostrar()
    def mostrar(self):
        return "\nRevista: \n" + super() + f", [Mes de publicación]: {self.getMesPublicacion()}, [Número de edición]: {self.getNumEdicion()}"