# Libro.py
# Clase Libro que hereda de la clase Material
# Richard Chadwick Plaza

from Material import Material

generos = ["ficción", "no ficción", "terror", "ciencia"]
generoPorDefefcto = "no ficción"

class Libro(Material):
    def __init__(self, id = 0, titulo = "", autor = "Anónimo", anioPublicacion = 0000, genero = generoPorDefefcto, numPaginas = 0):
        # Controlamos que el genero esta en la lista
        if genero.strip().lower() not in generos:
            raise ValueError("Error: el género del libro tiene que estar entre las siguientes posibilidades: (ficción, no ficción, terror, ciencia)")
        self.setGenero(genero.strip().lower())

        # Controlamos que el número de páginas sea un entero positivo
        if not isinstance(numPaginas, int) or numPaginas < 0:
            raise ValueError("Error el número de páginas debe ser un número entero positivo")
        self.setNumPaginas(numPaginas)

        # Inicializamos los atributos de la clase Padre
        super().__init__(id, titulo, autor, anioPublicacion)

    # Getters
    def getGenero(self):
        return self.__genero
        
    def getNumPaginas(self):
        return self.__numPaginas
        
    # Setters
    def setGenero(self, generoNuevo):
        if generoNuevo.strip().lower() not in generos:
            raise ValueError("Error: el género del libro tiene que estar entre las siguientes posibilidades: (ficción, no ficción, terror, ciencia)")
        self.__genero = generoNuevo.strip().lower()

    def setNumPaginas(self, numPaginasNuevo):
        if not isinstance(numPaginasNuevo, int) or numPaginasNuevo < 0:
            raise ValueError("Error el número de páginas debe ser un número entero positivo")
        self.__numPaginas = numPaginasNuevo

    # Sobrescribimos el mostrar()
    def mostrar(self):
        return "\nLibro: \n" + super() + f", [Género]: {self.getGenero()}, [Número de páginas]: {self.getNumPaginas()}"