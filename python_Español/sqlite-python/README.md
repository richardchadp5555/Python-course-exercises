# Bases de Datos con SQLite en Python 🌐

En este directorio exploraremos el manejo de **bases de datos relacionales** usando **SQLite** con Python. Aprenderás a conectar una base de datos, realizar operaciones CRUD (crear, leer, actualizar y eliminar), y gestionar datos de manera eficiente.

---

## Estructura del Proyecto 🗁

### **Carpetas principales**
- **`apuntes/`**: Aquí encontrarás los documentos de referencia y teoría compartidos por la profesora.
- **`databases/`**: Carpeta donde se almacenan las bases de datos SQLite utilizadas en los ejercicios.
- **`ejercicios/`**: Contiene los scripts de Python para cada ejercicio práctico.

---

## Ejercicios 🔢

### 1. **Crear y gestionar una tabla**
Archivo: `ejercicios/ejemplo1.py`

- Crear una base de datos SQLite.
- Definir y crear una tabla llamada `usuarios` con campos básicos como ID, nombre y edad.

### 2. **Insertar datos y realizar consultas**
Archivo: `ejercicios/ejemplo2.py`

- Insertar datos en la tabla creada.
- Consultar y mostrar los datos almacenados.

### 3. **Operaciones CRUD completas**
Archivo: `ejercicios/ejemplo3.py`

- Implementar las operaciones completas: crear, leer, actualizar y eliminar registros de la base de datos.

### 4. **Gestión de Tienda con SQLite 🛒**
Archivo: `ejercicios/ejercicio4-gestionTienda/`

- Implementa un sistema de gestión de tienda.
- Utiliza clases como `Producto` y `Tienda`.
- Permite operaciones CRUD con un menú interactivo.
- Integra manejo de excepciones y validaciones.

---

## Conceptos Fundamentales ⚖️

1. **SQLite**
   - Una base de datos ligera y fácil de usar, integrada directamente con Python mediante el módulo `sqlite3`.
   - Ideal para proyectos pequeños y pruebas locales.

2. **Operaciones CRUD**
   - **C**reate: Crear tablas y añadir datos.
   - **R**ead: Consultar y mostrar datos almacenados.
   - **U**pdate: Modificar datos existentes.
   - **D**elete: Eliminar datos de la base de datos.

3. **Gestión de la conexión**
   - Siempre abrir una conexión antes de realizar operaciones.
   - Confirmar los cambios con `commit()`.
   - Cerrar la conexión al finalizar para evitar problemas de acceso o pérdida de datos.

---

## Cómo ejecutar los ejercicios 🚀

### Desde Visual Studio Code
1. Abre el archivo del ejercicio que desees ejecutar en **Visual Studio Code**.
2. Haz clic en el botón **Run** (arriba a la derecha) o presiona `F5` para ejecutar el script.
3. Verifica los resultados en la terminal integrada de VS Code.

### Desde la consola o terminal (cmd, bash, etc.)
1. Navega al directorio del ejercicio que quieras ejecutar, por ejemplo:
   ```bash
   cd ejercicios
   ```
2. Ejecuta el script correspondiente con:
   ```bash
   python ejemplo1.py
   ```

---

## Requisitos 🔧
- **Python 3.8 o superior**.
- Un editor de código como **Visual Studio Code** o **PyCharm**.

---

## Recomendación: Usar la extensión SQLite en Visual Studio Code 📊

Para facilitar el manejo de bases de datos SQLite en tu proyecto, se recomienda instalar la extensión **SQLite** para Visual Studio Code.

### **Pasos para instalar y usar la extensión SQLite:**

1. **Instalar la extensión**:
   - Ve a la barra lateral de **Extensiones** en Visual Studio Code (Ctrl+Shift+X).
   - Busca "SQLite" (autor: alexcvzz).
   - Haz clic en **Instalar**.

2. **Abrir tu base de datos**:
   - Abre el panel de comandos con `Ctrl+Shift+P` (o `Cmd+Shift+P` en Mac).
   - Escribe `SQLite: Open Database` y selecciona esta opción.
   - Navega hasta tu base de datos (por ejemplo, `databases/base_datos_1.db`) y ábrela.

3. **Explorar la base de datos**:
   - En el panel lateral izquierdo, verás las tablas de la base de datos, su estructura (columnas) y podrás ejecutar consultas directamente.

### **Ventajas de usar esta extensión:**
- Explorar tablas y ver datos directamente desde Visual Studio Code.
- Ejecutar comandos SQL y ver resultados en tiempo real.
- Ideal para proyectos pequeños y educativos.

---

**Autor:** Richard Chadwick Plaza  
**Curso:** Segundo de DAM  
**Asignatura:** Python 💻
