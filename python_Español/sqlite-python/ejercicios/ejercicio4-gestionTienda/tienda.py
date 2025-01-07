# tienda.py
# Esta clase maneja las operaciones CRUD de productos en la base de datos
# Autor: Richard Chadwick Plaza
# Curso: Segundo DAM
# Lenguaje: Python

import sqlite3
from producto import Producto

class Tienda:
    def __init__(self, ruta_db):
        try:
            print(f"Intentando conectar con la base de datos en {ruta_db}...")
            self.conn = sqlite3.connect(ruta_db)
            self.cursor = self.conn.cursor()
            self.crear_tabla()
            print("Conexión a la base de datos establecida con éxito.")
        except sqlite3.Error as e:
            print(f"ERROR: No se pudo conectar a la base de datos: {e}")
            self.conn = None

    def crear_tabla(self):
        if not self.conn:
            print("ERROR: No se puede crear la tabla porque no hay conexión a la base de datos.")
            return
        try:
            self.cursor.execute('''
                CREATE TABLE IF NOT EXISTS productos(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nombre TEXT,
                    precio REAL,
                    stock INTEGER
                )
            ''')
            self.conn.commit()
        except sqlite3.Error as e:
            print(f"ERROR: No se pudo crear la tabla 'productos': {e}")

    def insertar_producto(self, producto):
        if not self.conn:
            print("ERROR: No se puede insertar porque no hay conexión a la base de datos.")
            return
        try:
            self.cursor.execute(
                'INSERT INTO productos (nombre, precio, stock) VALUES (?, ?, ?)',
                (producto.nombre, producto.precio, producto.stock)
            )
            self.conn.commit()
            print(f"Producto '{producto.nombre}' añadido con éxito.")
        except sqlite3.IntegrityError as e:
            print(f"ERROR: Violación de integridad al insertar el producto: {e}")
        except sqlite3.Error as e:
            print(f"ERROR: No se pudo insertar el producto: {e}")

    def consultar_productos(self):
        if not self.conn:
            print("ERROR: No se puede consultar porque no hay conexión a la base de datos.")
            return {}
        try:
            self.cursor.execute('SELECT * FROM productos')
            productos = self.cursor.fetchall()

            diccionario_productos = {}
            for prod in productos:
                id_producto = prod[0]
                nombre = prod[1]
                precio = prod[2]
                stock = prod[3]

                producto = Producto(id_producto, nombre, precio, stock)
                diccionario_productos[id_producto] = producto
            
            print("Productos disponibles:")
            for producto in diccionario_productos.values():
                print(producto)
            
            return diccionario_productos
        except sqlite3.Error as e:
            print(f"ERROR: No se pudo consultar los productos: {e}")
            return {}

    def actualizar_producto(self, id_producto, nuevo_nombre, nuevo_precio, nuevo_stock):
        if not self.conn:
            print("ERROR: No se puede actualizar porque no hay conexión a la base de datos.")
            return
        try:
            self.cursor.execute(
                'UPDATE productos SET nombre = ?, precio = ?, stock = ? WHERE id = ?',
                (nuevo_nombre, nuevo_precio, nuevo_stock, id_producto)
            )
            self.conn.commit()
            print(f"Producto con ID {id_producto} actualizado con éxito.")
        except sqlite3.Error as e:
            print(f"ERROR: No se pudo actualizar el producto con ID {id_producto}: {e}")

    def eliminar_producto(self, id_producto):
        if not self.conn:
            print("ERROR: No se puede eliminar porque no hay conexión a la base de datos.")
            return
        try:
            self.cursor.execute('DELETE FROM productos WHERE id = ?', (id_producto,))
            self.conn.commit()
            print(f"Producto con ID {id_producto} eliminado con éxito.")
        except sqlite3.Error as e:
            print(f"ERROR: No se pudo eliminar el producto con ID {id_producto}: {e}")

    def buscar_producto_por_id(self, id_producto):
        if not self.conn:
            print("ERROR: No se puede buscar porque no hay conexión a la base de datos.")
            return None
        try:
            self.cursor.execute('SELECT * FROM productos WHERE id = ?', (id_producto,))
            resultado = self.cursor.fetchone()

            if resultado:
                return Producto(resultado[0], resultado[1], resultado[2], resultado[3])
            else:
                return None
        except sqlite3.Error as e:
            print(f"ERROR: No se pudo buscar el producto con ID {id_producto}: {e}")
            return None

    def cerrar_conexion(self):
        try:
            if self.conn:
                self.conn.close()
                print("Conexión a la base de datos cerrada con éxito.")
            else:
                print("Conexión no establecida previamente.")
        except sqlite3.Error as e:
            print(f"ERROR: No se pudo cerrar la conexión a la base de datos: {e}")
