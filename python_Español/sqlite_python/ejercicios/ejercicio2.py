# Ejercicio 2: Insertar datos y realizar consultas
# -----------------------------------------------
# Objetivo:
# 1. Insertar registros en la tabla `usuarios`.
# 2. Consultar los registros de la tabla y mostrarlos en la consola.
# Autor: Richard Chadwick Plaza
# Tecnologías: Python y sqlite
# Fecha: 04/01/2025

import sqlite3

# Conexión
conn = sqlite3.connect('../databases/base_datos_1.db')

# Cursor
cursor = conn.cursor()

# usuarios para insertar
usuarios = [
    ('Juan', 25),
    ('Maria', 30),
    ('Carlos', 22)
]

# Insertamos los datos
cursor.executemany('INSERT INTO usuarios (nombre, edad) VALUES (?, ?)', usuarios)
print("Datos insertados correctamente. ")

# Consultar datos de la tabla usuarios
cursor.execute('SELECT * FROM usuarios')
registros = cursor.fetchall()

# Mostrar los registros
print("Registros en la tabla 'usuarios': ")
for registro in registros:
    print(registro)

# Confirmamos los cambios y cerramos la conexión
conn.commit()
conn.close()