# Ejercicio 3: Operaciones CRUD completas
# ---------------------------------------
# Objetivo:
# 1. Insertar nuevos registros en la tabla `usuarios`.
# 2. Consultar y mostrar los registros existentes.
# 3. Actualizar un registro.
# 4. Eliminar un registro.
# Autor: Richard Chadwick Plaza
# Tecnologías: Python y sqlite
# Fecha: 05/01/2025

import sqlite3

# Conexión
conn = sqlite3.connect('../databases/base_datos_1.db')
cursor = conn.cursor()

# CREATE: Insertar nuevos registros
def insertar_usuario(nombre, edad):
    cursor.execute('INSERT INTO usuarios (nombre, edad) VALUES (?, ?)', (nombre, edad))
    conn.commit()
    print(f"Usuario '{nombre}' añadido con éxito.")

# READ: Consultar todos los registros
def consultar_usuarios():
    cursor.execute('SELECT * FROM usuarios')
    registros = cursor.fetchall()
    print("Registros actuales de la tabla usuarios:")
    for registro in registros:
        print(registro)

# UPDATE: Modificar un registro ya existente
def actualizar_usuario(id_usuario, nuevo_nombre, nueva_edad):
    cursor.execute('UPDATE usuarios SET nombre = ?, edad = ? WHERE id = ?', (nuevo_nombre, nueva_edad, id_usuario))
    conn.commit()
    print(f"Usuario con ID {id_usuario} actualizado con éxito.")

# DELETE: eliminar un registro existente
def eliminar_usuario(id_usuario):
    cursor.execute('DELETE FROM usuarios WHERE id = ?', (id_usuario,))
    conn.commit()
    print(f"Usuario con ID {id_usuario} eliminado con éxito.")

# Ejecución de las operaciones
# Crear nuevos usuarios
insertar_usuario('Lucía', 28)
insertar_usuario('Miguel', 35)

# Consultar registros
consultar_usuarios()

# Actualizar un usuario
actualizar_usuario(1, 'Lucía Pérez', 29)

# Consultar registros nuevamente
consultar_usuarios()

# Eliminar un usuario
eliminar_usuario(2)

# Consultar registros finales
consultar_usuarios()

# Cerrar la conexión
conn.close()
