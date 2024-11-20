# Diccionarios en Python

En este directorio voy guardando ejercicios y ejemplos básicos para practicar el uso de diccionarios en Python. Los diccionarios son una estructura de datos mutable que almacena pares de clave-valor, y me permiten acceder a los datos de forma rápida usando una clave única.

## Archivos

- **diccionarios1.py**: En este archivo estoy probando diferentes operaciones con diccionarios, como:
  - Crear, acceder, modificar y eliminar elementos.
  - Verificar si una clave existe.
  - Copiar un diccionario con `copy()`.
  - Obtener el tamaño del diccionario con `len()`.

- **diccionarios2.py**: Ejemplos de algunos métodos esenciales al trabajar con diccionarios, como:
  - `clear()`: Elimina todos los elementos del diccionario.
  - `copy()`: Crea una copia superficial del diccionario.
  - `update()`: Añade los elementos de otro diccionario.
  - `get()`: Accede a un valor por su clave, con una opción de valor predeterminado si la clave no existe.
  - `pop()`: Elimina y devuelve el valor de una clave, con opción de valor predeterminado.
  - Recorrer el diccionario con `keys()`, `values()` e `items()`.

- **ejercicio_1_diccionarios.py**: Programa que pide al usuario una cadena de texto y devuelve un diccionario con el número de apariciones de cada carácter en la cadena.
- **ejercicio_2_diccionarios.py**: Programa que permite gestionar un inventario de frutas con precios fijos. Solicita al usuario el nombre de la fruta y la cantidad vendida, calcula el precio total y muestra el resultado. Incluye:
  - Validación de la existencia de la fruta en el diccionario.
  - Manejo de errores para entradas no numéricas en la cantidad.
  - Funcionalidad para repetir la consulta según la elección del usuario.
- **ejercicio_3_diccionarios.py**: Programa que implementa un listín telefónico utilizando un diccionario. 
  Ofrece las siguientes funcionalidades:
  - Mostrar el listín telefónico (orden por defecto y alfabético)
  - Añadir un nuevo contacto, comprobando que su teléfono sea un número de 9 dígitos
  - Modificar el telefono de un contacto existente
  - Eliminar un contacto
  - Borrar todo el listín
  - Un menú interactivo
- **ejercicio_4_diccionarios.py**: Programa que solicita al usuario su nombre, edad, dirección y teléfono, y guarda esta información en un diccionario. Después, muestra un mensaje con el formato:

- **ejercicio_5_diccionarios.py**: Programa que analiza las ventas diarias y mensuales de una tienda a partir de un diccionario que contiene las ventas de cuatro productos durante 30 días. Incluye las siguientes funcionalidades:
  - Calcular y mostrar el total de unidades vendidas en el mes para cada producto.
  - Identificar el producto más vendido y el menos vendido del mes.
  - Mostrar las ventas diarias del producto más vendido.
  - Determinar el día con la mayor cantidad de ventas para cada producto.

  ### Notas sobre el enfoque del programa:
  Este programa no permite modificar los datos de ventas ni añadir nuevos productos, por lo que las opciones del menú solo muestran información preexistente. Para optimizar el rendimiento y evitar cálculos innecesarios, se precalculan los totales y los extremos de ventas antes de que el usuario interactúe con el menú. Esto garantiza eficiencia y claridad en los resultados, ya que no es necesario recalcular información que no cambia durante la ejecución del programa.

---

Este directorio es parte de mi material de estudio personal en Python, donde guardo ejercicios para afianzar conceptos y experimentar con código.

---

## Requisitos
- **Python 3.8 o superior**.
- Un editor de código como **Visual Studio Code** o **PyCharm**.

---

**Autor:** Richard Chadwick Plaza  
**Curso:** Segundo de DAM  
**Asignatura:** Python
