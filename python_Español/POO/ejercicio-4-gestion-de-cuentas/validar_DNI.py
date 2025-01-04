# validar_DNI.py
# En este archivo se define una función que permite comprobar si un dni tiene el formato adecuado o no.
# Si no tiene el formato adecuado devuelve 'False' y, si cumple con las condiciones, devuelve 'True'
# Richard Chadwick Plaza            2ºDAM

import re

# Función para comprobar que el DNI tenga el formato adecuado usando una expresión regular
def validarDni(dni):
    LETRAS = "TRWAGMYFPDXBNJZSQVHLCKE"
    dni = dni.strip().upper()  # Eliminamos espacios y aseguramos mayúsculas

    # Validamos el formato con una expresión regular
    if not re.match(r"^\d{8}[A-Z]$", dni):
        return False

    # Si el dni cumple el formato, comprobamos que la letra sea válida
    numero = int(dni[:-1])  # Los primeros 8 caracteres son el número
    letra = dni[-1]  # El último carácter es la letra

    # Comprobamos que la letra sea la correcta
    return LETRAS[numero % 23] == letra
