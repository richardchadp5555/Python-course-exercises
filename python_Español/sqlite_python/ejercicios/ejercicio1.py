# Ejercicio 1: Crear y gestionar una tabla
# ---------------------------------------
# Objetivo:
# 1. Conectarse a una base de datos SQLite llamada `mi_base.db` (ubicada en la carpeta `databases/`).
# 2. Crear una tabla llamada `usuarios` si no existe.
#    - La tabla debe tener las siguientes columnas:
#      - id: Número entero, clave primaria, autoincremental.
#      - nombre: Texto, para almacenar el nombre de los usuarios.
#      - edad: Número entero, para almacenar la edad.
# 3. Confirmar la creación de la tabla e informar al usuario mediante un mensaje en consola.
# 4. Cerrar la conexión con la base de datos.
# Autor: Richard Chadwick Plaza
# Tecnologías: Python y sqlite
# Fecha: 04/01/2025

import sqlite3 # Importamos el módulo apra trabajar con sqlite

# 1. Conexión
conn = sqlite3.connect('../databases/base_datos_1.db')

# 2. Creamos un cursor para ejecutar sentencias SQL
cursor = conn.cursor()

# 3. Creamos una tabla usuarios
cursor.execute('''
CREATE TABLE IF NOT EXISTS usuarios(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT,
    edad INTEGER
)
''')

# 4. Confirmamos los cambios
conn.commit()

# 5. Cerrar la conexión
conn.close()

# 6. Informamos por pantalla de la creación de la tabla
print("Tabla usuarios creada con éxito")