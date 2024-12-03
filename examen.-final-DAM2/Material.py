# Material.py
# Clase Material, clase padre del programa con atributos comunes 
# Richard Chadwick Plaza

# Para controlar que cada material tenga su id propio, el prorgama asignará automaticamente un id autoincrementado



class Material():
    def __init__(self, id = 0, titulo = "", autor = "Anónimo", anioPublicacion = 0000):
        self.setId(id)
        self.setTitulo(titulo)
        self.setAutor(autor)
        self.setAnioPublicacion(anioPublicacion)


    # GETTERS
    def getId(self):
        return self.__id
        
    def getTitulo(self):
        return self.__titulo
        
    def getAutor(self):
        return self.__autor
        
    def getAnioPublicacion(self):
        return self.__anioPublicacion

    # SETTERS
    def setId(self, id):
        self.__id = id

    def setTitulo(self, tituloNuevo):
        if not tituloNuevo.strip():
            raise ValueError("Error: el título no puede ser un campo vacío. ")
        self.__titulo = tituloNuevo
        
    def setAutor(self, autorNuevo):
        if not autorNuevo.strip():
            raise ValueError("Error: el autor no debe ser un campo vacío")
        self.__autor = autorNuevo
        
    def setAnioPublicacion(self, anio):
        if anio < 0:
            raise ValueError("Error el año de publicación no puede ser un número negativo")
        
    # Método toString para mostrar el objeto y sus atributos
    def mostrar(self):
        return {f"[ID] = {self.getId()}, [Titulo] = {self.getTitulo()}, [Autor] = {self.getAutor()}, [Año de publicación] = {self.getAnioPublicacion}"}