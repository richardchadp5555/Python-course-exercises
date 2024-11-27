# utilidadesListas.py
# Este archivo contiene utilidades avanzadas y métodos comunes para trabajar con listas en Python.
# Incluye operaciones básicas, filtrado, búsqueda, ordenación, agrupación y eliminación de duplicados.
# Autor: Richard Chadwick Plaza        Curso: 2ºDAM       Python

# ==========================
# OPERACIONES BÁSICAS CON LISTAS
# ==========================

def operacionesBasicas():
    """
    Ejemplo de operaciones básicas con listas en Python.
    """
    # Crear una lista vacía
    lista = []
    print("Lista vacía:", lista)

    # Añadir elementos a una lista
    lista.append("Elemento 1")
    lista.append("Elemento 2")
    print("Lista después de añadir elementos:", lista)

    # Insertar un elemento en una posición específica
    lista.insert(1, "Elemento 1.5")  # Insertar en la posición 1
    print("Lista después de insertar un elemento:", lista)

    # Eliminar un elemento por su valor
    lista.remove("Elemento 1")  # Elimina la primera aparición
    print("Lista después de eliminar un elemento por su valor:", lista)

    # Eliminar un elemento por su posición
    elementoEliminado = lista.pop(1)  # Elimina y devuelve el elemento en la posición 1
    print(f"Lista después de eliminar el elemento en la posición 1: {lista}. Elemento eliminado: {elementoEliminado}")

    # Concatenar dos listas
    lista2 = ["Elemento 3", "Elemento 4"]
    listaConcatenada = lista + lista2
    print("Lista concatenada:", listaConcatenada)

    # Extender una lista con otra
    lista.extend(lista2)
    print("Lista después de extenderla con otra lista:", lista)

    # Obtener el tamaño de una lista
    print("Tamaño de la lista:", len(lista))

    # Comprobar si un elemento está en una lista
    print("¿'Elemento 3' está en la lista?:", "Elemento 3" in lista)

    # Limpiar la lista
    lista.clear()
    print("Lista después de limpiarla:", lista)

# ==========================
# MÉTODOS ÚTILES PARA LISTAS
# ==========================

# Crear una lista con un rango de números
def crearListaRango(inicio, fin):
    """
    Crea una lista con números desde el inicio hasta el fin (inclusive).
    Args:
        inicio (int): Número inicial.
        fin (int): Número final.
    Returns:
        list: Lista de números.
    """
    return list(range(inicio, fin + 1))


# Filtrar elementos de una lista según una condición
def filtrarLista(lista, condicion):
    """
    Filtra una lista según una condición dada.
    Args:
        lista (list): Lista a filtrar.
        condicion (function): Función que define la condición.
    Returns:
        list: Lista filtrada.
    """
    return [elemento for elemento in lista if condicion(elemento)]


# Ordenar una lista de números o cadenas
def ordenarLista(lista, descendente=False):
    """
    Ordena una lista en orden ascendente o descendente.
    Args:
        lista (list): Lista a ordenar.
        descendente (bool): Si True, ordena en orden descendente.
    Returns:
        list: Lista ordenada.
    """
    return sorted(lista, reverse=descendente)


# Ordenar una lista de objetos Persona por nombre o edad
def ordenarPersonas(personas, atributo, descendente=False):
    """
    Ordena una lista de objetos Persona por un atributo específico (nombre o edad).
    Args:
        personas (list): Lista de objetos Persona.
        atributo (str): Atributo por el cual ordenar ("nombre" o "edad").
        descendente (bool): Si True, ordena en orden descendente.
    Returns:
        list: Lista ordenada de objetos Persona.
    """
    return sorted(personas, key=lambda persona: getattr(persona, atributo), reverse=descendente)


# Buscar un elemento en una lista (devuelve el índice o -1 si no existe)
def buscarElemento(lista, elemento):
    """
    Busca un elemento en una lista.
    Args:
        lista (list): Lista donde buscar.
        elemento: Elemento a buscar.
    Returns:
        int: Índice del elemento o -1 si no existe.
    """
    try:
        return lista.index(elemento)
    except ValueError:
        return -1


# Buscar objetos Persona por nombre
def buscarPersonaPorNombre(personas, nombre):
    """
    Busca personas en una lista de objetos Persona por su nombre.
    Args:
        personas (list): Lista de objetos Persona.
        nombre (str): Nombre a buscar.
    Returns:
        list: Lista de objetos Persona con el nombre indicado.
    """
    return [persona for persona in personas if persona.nombre == nombre]


# Eliminar duplicados de una lista
def eliminarDuplicados(lista):
    """
    Elimina elementos duplicados de una lista.
    Args:
        lista (list): Lista original con posibles duplicados.
    Returns:
        list: Lista sin duplicados.
    """
    return list(set(lista))


# Agrupar elementos de una lista por una función clave
def agruparPor(lista, clave):
    """
    Agrupa elementos de una lista según una función clave.
    Args:
        lista (list): Lista a agrupar.
        clave (function): Función que define el criterio de agrupación.
    Returns:
        dict: Diccionario donde las claves son los grupos y los valores son listas de elementos.
    """
    agrupado = {}
    for elemento in lista:
        grupo = clave(elemento)
        if grupo not in agrupado:
            agrupado[grupo] = []
        agrupado[grupo].append(elemento)
    return agrupado


# ==========================
# MÉTODOS PARA EJERCICIOS COMUNES
# ==========================

# Crear una lista de objetos Persona
def crearListaPersonas():
    """
    Crea una lista de objetos Persona con datos de ejemplo.
    Returns:
        list: Lista de objetos Persona.
    """
    return [
        Persona("Richard", 30),
        Persona("Ana", 25),
        Persona("Juan", 40),
        Persona("Ana", 20),
    ]


# Filtrar personas mayores de edad
def filtrarMayoresDeEdad(personas):
    """
    Filtra una lista de objetos Persona y devuelve solo los mayores de edad.
    Args:
        personas (list): Lista de objetos Persona.
    Returns:
        list: Lista de mayores de edad.
    """
    return filtrarLista(personas, lambda p: p.edad >= 18)


# Calcular la suma de los elementos de una lista
def sumaLista(lista):
    """
    Calcula la suma de los elementos de una lista de números.
    Args:
        lista (list): Lista de números.
    Returns:
        int: Suma de los elementos.
    """
    return sum(lista)


# Encontrar el valor máximo en una lista
def valorMaximo(lista):
    """
    Encuentra el valor máximo de una lista.
    Args:
        lista (list): Lista de números.
    Returns:
        int: Valor máximo.
    """
    return max(lista)


# Encontrar el valor mínimo en una lista
def valorMinimo(lista):
    """
    Encuentra el valor mínimo de una lista.
    Args:
        lista (list): Lista de números.
    Returns:
        int: Valor mínimo.
    """
    return min(lista)


# ==========================
# CLASE Persona PARA EJEMPLOS
# ==========================
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def __str__(self):
        return f"Persona: [Nombre: {self.nombre}, Edad: {self.edad}]"


# ==========================
# DEMOSTRACIÓN DE USO
# ==========================
if __name__ == "__main__":
    print("=== Operaciones Básicas ===")
    operacionesBasicas()

    # Ejemplo avanzado con objetos
    print("\n=== Ejemplo Avanzado con Objetos ===")
    personas = crearListaPersonas()
    mayores = filtrarMayoresDeEdad(personas)
    print("Mayores de edad:")
    for p in mayores:
        print(p)
