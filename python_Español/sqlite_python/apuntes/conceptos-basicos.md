# Conceptos Básicos de SQLite con Python

SQLite es una base de datos ligera y embebida, ideal para proyectos pequeños o para aprender a trabajar con bases de datos relacionales en Python. Aquí te presentamos los conceptos clave para empezar.

---

## Pasos para trabajar con SQLite en Python

1. **Conectar** a una base de datos:
   - Se utiliza `sqlite3.connect()` para conectarse o crear una base de datos:
     ```python
     conn = sqlite3.connect('mi_base.db')
     ```
     Si el archivo de base de datos no existe, Python lo crea automáticamente.

2. **Crear un cursor**:
   - El cursor es el objeto que se usa para ejecutar comandos SQL:
     ```python
     cursor = conn.cursor()
     ```

3. **Ejecutar comandos SQL**:
   - Por ejemplo, para crear una tabla:
     ```python
     cursor.execute('''
     CREATE TABLE IF NOT EXISTS usuarios (
         id INTEGER PRIMARY KEY AUTOINCREMENT,
         nombre TEXT,
         edad INTEGER
     )
     ''')
     ```

4. **Confirmar cambios**:
   - Después de ejecutar comandos que alteran la base de datos (como INSERT, UPDATE o DELETE), es necesario confirmar los cambios:
     ```python
     conn.commit()
     ```

5. **Cerrar la conexión**:
   - Es importante cerrar la conexión para liberar recursos:
     ```python
     conn.close()
     ```

---

## Ejemplo básico

El siguiente ejemplo muestra cómo crear una base de datos y una tabla llamada `usuarios`:

```python
import sqlite3

# 1. Conexión a la base de datos
conn = sqlite3.connect('mi_base.db')

# 2. Crear un cursor
cursor = conn.cursor()

# 3. Crear una tabla
cursor.execute('''
CREATE TABLE IF NOT EXISTS usuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT,
    edad INTEGER
)
''')

# 4. Confirmar los cambios
conn.commit()

# 5. Cerrar la conexión
conn.close()

print("Tabla 'usuarios' creada con éxito.")
```

---

## Recomendaciones

1. **Evita usar comandos SQL sin validación**:
   - Usa parámetros para prevenir inyecciones SQL:
     ```python
     cursor.execute('INSERT INTO usuarios (nombre, edad) VALUES (?, ?)', ('Juan', 30))
     ```

2. **Manejo de errores**:
   - Usa bloques `try-except` para manejar errores de conexión o ejecución:
     ```python
     try:
         conn = sqlite3.connect('mi_base.db')
         cursor = conn.cursor()
         # Operaciones con la base de datos
     except sqlite3.Error as e:
         print(f"Error: {e}")
     finally:
         if conn:
             conn.close()
     
