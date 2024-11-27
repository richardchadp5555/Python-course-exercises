# metodosAvanzadosDiccionarios.py
# Este archivo contiene métodos avanzados y ejemplos prácticos para trabajar con diccionarios en Python.
# Incluye operaciones de ordenación, búsqueda, filtrado, agrupación y manejo de excepciones, así como interacciones con objetos.
# Autor: Richard Chadwick Plaza      Curso: 2ºDAM      Python

# ==========================
# EXPLICACIÓN: hasattr y getattr
# ==========================

"""
En Python, `hasattr` y `getattr` son funciones para trabajar dinámicamente con los atributos de un objeto.

- `hasattr(objeto, "atributo")`:
  Verifica si un objeto tiene un atributo con el nombre especificado.
  Retorna `True` si el atributo existe, `False` en caso contrario.

- `getattr(objeto, "atributo", valor_por_defecto)`:
  Obtiene el valor de un atributo de un objeto.
  Si el atributo no existe:
    1. Retorna el valor por defecto (si se especifica).
    2. Lanza un error `AttributeError` (si no se especifica valor por defecto).

Ejemplo práctico:
"""

# Clase de ejemplo
class Persona:
    def __init__(self, nombre, edad, telefono):
        self.nombre = nombre
        self.edad = edad
        self.telefono = telefono

    def __str__(self):
        return f"Nombre: {self.nombre}, Edad: {self.edad}, Teléfono: {self.telefono}"

# Crear un objeto Persona
persona = Persona("Juan", 30, "123456789")

# Verificar si el objeto tiene un atributo con hasattr
if hasattr(persona, "nombre"):
    print("El atributo 'nombre' existe.")  # Esto se imprimirá

if not hasattr(persona, "direccion"):
    print("El atributo 'direccion' no existe.")  # Esto se imprimirá

# Obtener un valor de un atributo con getattr
nombre = getattr(persona, "nombre")  # Devuelve "Juan"
print(f"Nombre: {nombre}")

# Usar getattr con un valor por defecto
direccion = getattr(persona, "direccion", "No especificada")  # Devuelve "No especificada"
print(f"Dirección: {direccion}")

# ==========================
# ORDENAR DICCIONARIOS
# ==========================

def ordenarDiccionarioPorClave(dicc, descendente=False):
    """
    Ordena un diccionario por sus claves.
    Args:
        dicc (dict): Diccionario a ordenar.
        descendente (bool): Si True, ordena en orden descendente.
    Returns:
        dict: Diccionario ordenado por claves.
    """
    return dict(sorted(dicc.items(), key=lambda x: x[0], reverse=descendente))


def ordenarDiccionarioPorValor(dicc, descendente=False):
    """
    Ordena un diccionario por sus valores.
    Args:
        dicc (dict): Diccionario a ordenar.
        descendente (bool): Si True, ordena en orden descendente.
    Returns:
        dict: Diccionario ordenado por valores.
    """
    return dict(sorted(dicc.items(), key=lambda x: x[1], reverse=descendente))


# ==========================
# FILTRAR DICCIONARIOS
# ==========================

def filtrarDiccionarioPorValor(dicc, valor_minimo):
    """
    Filtra los elementos de un diccionario cuyos valores sean mayores o iguales a un valor mínimo.
    Args:
        dicc (dict): Diccionario a filtrar.
        valor_minimo: Valor mínimo para incluir.
    Returns:
        dict: Diccionario filtrado.
    """
    filtrado = {}
    for clave, valor in dicc.items():
        if valor >= valor_minimo:
            filtrado[clave] = valor
    return filtrado


def filtrarDiccionarioPorClave(dicc, texto):
    """
    Filtra un diccionario cuyas claves contengan un texto específico.
    Args:
        dicc (dict): Diccionario a filtrar.
        texto (str): Texto que deben contener las claves.
    Returns:
        dict: Diccionario filtrado.
    """
    filtrado = {}
    for clave, valor in dicc.items():
        if texto in clave:
            filtrado[clave] = valor
    return filtrado


# ==========================
# AGRUPAR DICCIONARIOS
# ==========================

def agruparPorRangos(dicc, rango):
    """
    Agrupa las claves y valores de un diccionario en rangos específicos basados en los valores.
    Args:
        dicc (dict): Diccionario a agrupar.
        rango (int): Tamaño del rango.
    Returns:
        dict: Diccionario agrupado.
    """
    agrupado = {}
    for clave, valor in dicc.items():
        grupo = (valor // rango) * rango
        if grupo not in agrupado:
            agrupado[grupo] = []
        agrupado[grupo].append((clave, valor))
    return agrupado


# ==========================
# BÚSQUEDA EN DICCIONARIOS
# ==========================

def buscarClave(dicc, clave):
    """
    Busca una clave en el diccionario y devuelve su valor.
    Args:
        dicc (dict): Diccionario donde buscar.
        clave: Clave a buscar.
    Returns:
        Valor asociado a la clave o None si no existe.
    """
    return dicc.get(clave, None)


def buscarValoresIguales(dicc, valor):
    """
    Busca claves que tengan un valor específico en el diccionario.
    Args:
        dicc (dict): Diccionario donde buscar.
        valor: Valor a buscar.
    Returns:
        list: Lista de claves con el valor buscado.
    """
    return [clave for clave, val in dicc.items() if val == valor]


# ==========================
# INTERACCIÓN CON OBJETOS
# ==========================

def buscarObjetosPorAtributo(dicc, atributo, valor):
    """
    Busca objetos en un diccionario con un atributo que coincida con un valor específico.
    Args:
        dicc (dict): Diccionario de objetos.
        atributo (str): Nombre del atributo.
        valor: Valor a buscar.
    Returns:
        list: Lista de objetos que cumplen la condición.
    """
    resultados = []
    for obj in dicc.values():
        if hasattr(obj, atributo) and getattr(obj, atributo) == valor:
            resultados.append(obj)
    return resultados


def agruparObjetosPorAtributo(dicc, atributo):
    """
    Agrupa objetos en un diccionario según el valor de uno de sus atributos.
    Args:
        dicc (dict): Diccionario de objetos.
        atributo (str): Atributo para agrupar.
    Returns:
        dict: Diccionario agrupado por atributos.
    """
    agrupado = {}
    for obj in dicc.values():
        if hasattr(obj, atributo):
            clave = getattr(obj, atributo)
            if clave not in agrupado:
                agrupado[clave] = []
            agrupado[clave].append(obj)
    return agrupado


# ==========================
# FUNCIONES COMPLEMENTARIAS
# ==========================

def combinarDiccionarios(dicc1, dicc2):
    """
    Combina dos diccionarios. Si hay claves duplicadas, se sobreescriben con el valor de dicc2.
    Args:
        dicc1 (dict): Primer diccionario.
        dicc2 (dict): Segundo diccionario.
    Returns:
        dict: Diccionario combinado.
    """
    combinado = dicc1.copy()
    combinado.update(dicc2)
    return combinado


def invertirDiccionario(dicc):
    """
    Invierte un diccionario, intercambiando claves por valores.
    Args:
        dicc (dict): Diccionario a invertir.
    Returns:
        dict: Diccionario invertido.
    """
    return {valor: clave for clave, valor in dicc.items()}


# ==========================
# EXCEPCIONES Y VALIDACIONES
# ==========================

def validarExistenciaClave(dicc, clave):
    """
    Comprueba si una clave existe en un diccionario.
    Args:
        dicc (dict): Diccionario donde buscar.
        clave: Clave a comprobar.
    Returns:
        bool: True si la clave existe, False en caso contrario.
    """
    return clave in dicc


def manejarExcepcionClave(dicc, clave):
    """
    Maneja excepciones al intentar acceder a una clave inexistente.
    Args:
        dicc (dict): Diccionario donde buscar.
        clave: Clave a buscar.
    Returns:
        Valor asociado a la clave o un mensaje de error.
    """
    try:
        return dicc[clave]
    except KeyError:
        return f"Error: La clave '{clave}' no existe en el diccionario."


# ==========================
# FIN DEL ARCHIVO
# ==========================
