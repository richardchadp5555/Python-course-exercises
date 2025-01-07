# Ejercicio 4: Gestión de Tienda con SQLite en Python 🏦

En este ejercicio, se implementa un sistema de gestión de tienda utilizando bases de datos SQLite, junto con clases y objetos en Python.

---

## Enunciado

**Objetivo del ejercicio:**
1. Crear un sistema para gestionar los productos de una tienda, utilizando una base de datos SQLite.
2. Implementar las siguientes operaciones CRUD (Crear, Leer, Actualizar, Eliminar):
   - Insertar un producto.
   - Consultar todos los productos.
   - Actualizar un producto.
   - Eliminar un producto.
3. Utilizar clases y objetos para representar la tienda y los productos.
4. Usar un menú interactivo para que el usuario pueda realizar las operaciones.

---

## Estructura del Ejercicio

El ejercicio se organiza en dos clases principales:

1. **Clase `Producto`:**
   - Representa los productos de la tienda.
   - Cada producto tiene los atributos:
     - `id`: Identificador único (generado automáticamente por SQLite).
     - `nombre`: Nombre del producto.
     - `precio`: Precio del producto.
     - `stock`: Cantidad disponible.

2. **Clase `Tienda`:**
   - Gestiona las operaciones CRUD sobre los productos en la base de datos.
   - Está conectada a un archivo SQLite que almacena los datos de los productos.
   - Implementa métodos para:
     - Crear la tabla `productos`.
     - Insertar productos.
     - Consultar todos los productos.
     - Actualizar un producto por su ID.
     - Eliminar un producto por su ID.
     - Buscar un producto por su ID.

Además, se incluye un archivo `main.py` que proporciona un menú interactivo para gestionar la tienda.

---

## Estructura del Proyecto 📂

El proyecto tiene la siguiente estructura de archivos y carpetas:

```plaintext
|-- ejercicio4-gestionTienda/
    |-- __pycache__/         # Archivos generados automáticamente por Python
    |-- tienda.db       # Base de datos SQLite 
    |-- main.py             # Archivo principal con el menú interactivo
    |-- producto.py         # Clase Producto
    |-- tienda.py           # Clase Tienda que gestiona las operaciones
```

---

## Tecnologías Usadas 💡

- **Python**: Lenguaje de programación principal para implementar las clases y el menú interactivo.
- **SQLite**: Base de datos embebida para almacenar y gestionar los productos de la tienda.

---

## Consejos y Notas Importantes 🚀

1. **Rutas Relativas:**
   - Asegúrate de ejecutar el archivo `main.py` desde su misma ubicación para que las rutas relativas funcionen correctamente.
   - Si prefieres rutas absolutas, puedes usar el módulo `os` para calcular la ruta absoluta de la base de datos.

2. **Validación de Datos:**
   - El programa incluye validaciones para asegurarse de que los datos introducidos por el usuario sean válidos (por ejemplo, que el precio sea numérico).
   - Si el usuario introduce valores inválidos, el programa muestra mensajes de error claros.

3. **Gestín de Errores SQL:**
   - Todos los métodos de la clase `Tienda` incluyen bloques `try-except` para capturar y manejar errores de SQLite.
   - Esto asegura que el programa no se detenga abruptamente si ocurre un error en la base de datos.

4. **Consulta de Productos:**
   - La operación de consulta convierte los resultados de la base de datos en objetos de tipo `Producto` para facilitar su manejo.

---

## Ejemplo de Ejecución 🎮

**1. Menú Principal:**
Al ejecutar `main.py`, el usuario verá un menú con las siguientes opciones:

```plaintext
Bienvenido! ¿Qué quieres hacer?
1. Insertar un producto.
2. Consultar los productos de la tienda.
3. Actualizar un producto.
4. Eliminar un producto.
5. Salir.
Introduce una opción:
```

**2. Inserción de Productos:**
El usuario introduce el nombre, precio y stock del producto. El programa lo guarda en la base de datos.

**3. Consulta de Productos:**
El programa muestra una lista de los productos disponibles en la tienda.

**4. Actualización de Productos:**
El usuario introduce el ID del producto que desea actualizar y los nuevos valores. Si no desea cambiar un atributo, puede dejarlo en blanco para conservar su valor actual.

**5. Eliminación de Productos:**
El usuario introduce el ID del producto que desea eliminar. El programa muestra una confirmación antes de proceder.

---

## Explicaciones de Implementación 🔧

1. **Clase Producto:**
   - Es simple y se encarga de encapsular los datos de un producto.
   - Incluye un método `__str__` para representar al producto como una cadena legible.

2. **Clase Tienda:**
   - Gestiona todas las operaciones relacionadas con la base de datos.
   - Incluye validaciones para asegurarse de que la conexión a la base de datos esté establecida antes de ejecutar una operación.

3. **Menú Interactivo:**
   - Usa la estructura `match-case` para manejar las opciones del usuario de manera clara y ordenada.
   - Incluye mensajes de confirmación para operaciones sensibles como actualizaciones y eliminaciones.

---

## Para Ejecutar el Ejercicio 🔄

1. Asegúrate de tener Python instalado.
2. Ejecuta el archivo `main.py` desde la terminal:
   ```bash
   python main.py
   ```
3. Sigue las instrucciones del menú para realizar las operaciones.

---

**Autor:** Richard Chadwick Plaza  
**Curso:** Segundo DAM  
**Asignatura:** Python
