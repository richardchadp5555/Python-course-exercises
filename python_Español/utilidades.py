# utilidades.py
# Plantilla con funciones y métodos útiles para trabajar con Python.
# Incluye métodos para diccionarios, listas, clases y validaciones.
# Autor: Richard Chadwick Plaza       Curso: 2ºDAM       Python

import re

# ==========================
# VALIDACIONES
# ==========================

# Valida un DNI español
def validarDni(dni):
    """
    Valida un DNI español.
    Requisitos:
    - Formato: 8 dígitos seguidos de una letra (ejemplo: 12345678Z).
    - La letra debe ser válida según el cálculo del resto del número entre 23.

    Args:
        dni (str): DNI a validar.

    Returns:
        bool: True si el DNI es válido, False en caso contrario.
    """
    LETRAS = "TRWAGMYFPDXBNJZSQVHLCKE"
    dni = dni.strip().upper()

    if not re.match(r"^\d{8}[A-Z]$", dni):
        return False

    numero = int(dni[:-1])
    letra = dni[-1]
    return LETRAS[numero % 23] == letra

# Valida si un teléfono tiene 9 dígitos
def validarTelefono(telefono):
    """
    Valida si un número de teléfono tiene exactamente 9 dígitos.
    """
    return re.fullmatch(r"^\d{9}$", telefono) is not None

# Valida un teléfono de forma mas estricta
def validarTelefonoStricto(telefono):
    """
    Valida si un número de teléfono español es correcto.
    Requisitos:
    - Debe tener 9 dígitos.
    - Debe comenzar con 6, 7 o 9.
    """
    return re.fullmatch(r"^[679]\d{8}$", telefono) is not None

# ==========================
# FUNCIONES PARA DICCIONARIOS
# ==========================

# Ordena un diccionario por clave. Si descendente es True se ordena de forma descendente
def ordenarDiccionarioPorClave(dicc, descendente=False):
    """
    Ordena un diccionario por clave en orden ascendente o descendente.
    """
    return dict(sorted(dicc.items(), key=lambda x: x[0], reverse=descendente))

# ordena un diccionario por su valor. Si decendente es True se ordena de forma descendente
def ordenarDiccionarioPorValor(dicc, descendente=False):
    """
    Ordena un diccionario por valor en orden ascendente o descendente.
    """
    return dict(sorted(dicc.items(), key=lambda x: x[1], reverse=descendente))

# Invierte las claves y los valores de un diccionario
def invertirDiccionario(dicc):
    """
    Invierte las claves y valores de un diccionario.
    """
    return {valor: clave for clave, valor in dicc.items()}

# Sirve para mostrar por pantalla un diccionario
def mostrarDiccionario(dicc):
    """
    Muestra el contenido de un diccionario en un formato legible.
    """
    for clave, valor in dicc.items():
        print(f"Clave: {clave} -> Valor: {valor}")