# utilidadesDiccionarios.py
# MÉTODOS Y FUNCIONES PARA DICCIONARIOS
# Lista de métodos útiles para trabajar con diccionarios en Python.
# Incluye ejemplos y descripciones de cada método.
# Autor: Richard Chadwick Plaza     2ºDAM       Python
# Crear un diccionario
mi_diccionario = {"a": 1, "b": 2, "c": 3}

# ==========================
# OBTENER VALORES
# ==========================

# Obtener el valor asociado a una clave
valor = mi_diccionario.get("a")  # Devuelve 1
# Si la clave no existe, devuelve None (o un valor por defecto si se especifica):
valor_por_defecto = mi_diccionario.get("d", "No encontrado")  # Devuelve "No encontrado"

# Acceso directo (lanza KeyError si no existe):
valor_directo = mi_diccionario["a"]  # Devuelve 1

# ==========================
# AÑADIR O ACTUALIZAR ELEMENTOS
# ==========================

# Añadir o actualizar un elemento
mi_diccionario["d"] = 4  # Añade {"d": 4} al diccionario
mi_diccionario["a"] = 10  # Actualiza el valor de "a" a 10

# Actualizar varios elementos (o combinar diccionarios)
otros_datos = {"e": 5, "f": 6}
mi_diccionario.update(otros_datos)  # Combina los diccionarios

# ==========================
# ELIMINAR ELEMENTOS
# ==========================

# Eliminar un elemento por su clave (y obtener su valor)
valor_eliminado = mi_diccionario.pop("a")  # Devuelve 10, y elimina la clave "a"

# Eliminar un elemento aleatorio
clave_valor = mi_diccionario.popitem()  # Devuelve una tupla como ("d", 4)

# Eliminar todos los elementos
mi_diccionario.clear()  # Deja el diccionario vacío

# ==========================
# CONSULTAR INFORMACIÓN
# ==========================

# Ver todas las claves
claves = mi_diccionario.keys()  # Devuelve dict_keys(['b', 'c', 'e', 'f'])

# Ver todos los valores
valores = mi_diccionario.values()  # Devuelve dict_values([2, 3, 5, 6])

# Ver todas las claves y valores
pares = mi_diccionario.items()  # Devuelve dict_items([('b', 2), ('c', 3), ('e', 5), ('f', 6)])

# Saber si una clave existe en el diccionario
existe = "b" in mi_diccionario  # Devuelve True
no_existe = "z" not in mi_diccionario  # Devuelve True

# Ver el número de elementos
tamaño = len(mi_diccionario)  # Devuelve 4

# ==========================
# ITERAR SOBRE EL DICCIONARIO
# ==========================

# Iterar por claves
for clave in mi_diccionario:
    print(f"Clave: {clave}")

# Iterar por valores
for valor in mi_diccionario.values():
    print(f"Valor: {valor}")

# Iterar por pares clave-valor
for clave, valor in mi_diccionario.items():
    print(f"Clave: {clave}, Valor: {valor}")

# ==========================
# FUNCIONES ÚTILES
# ==========================

# Crear un diccionario vacío
nuevo_diccionario = dict()  # También puedes usar {}

# Crear un diccionario con claves y un valor por defecto
diccionario_por_defecto = dict.fromkeys(["a", "b", "c"], 0)  # {'a': 0, 'b': 0, 'c': 0}

# Copiar un diccionario
copia_diccionario = mi_diccionario.copy()  # Devuelve una copia independiente

# ==========================
# EJEMPLOS EXTRA
# ==========================

# Filtrar elementos de un diccionario
# Ejemplo: Crear un nuevo diccionario con claves cuyos valores sean mayores que 3
filtrado = {k: v for k, v in mi_diccionario.items() if v > 3}

# Ordenar un diccionario por longitud de clave
ordenado_por_longitud = dict(sorted(mi_diccionario.items(), key=lambda x: len(x[0])))

# Combinar múltiples diccionarios en uno solo (a partir de Python 3.9)
diccionario_combinado = {**mi_diccionario, **otros_datos}  # Combina claves y valores

