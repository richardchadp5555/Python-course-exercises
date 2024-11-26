## ejercicio-3-diccionario-de-contactos

#  📄 Diccionario de Contactos con POO

Este proyecto consiste en un programa desarrollado en Python que gestiona un diccionario de contactos utilizando Programación Orientada a Objetos (POO). Se implementa la clase `Persona` para representar a cada contacto, y un programa principal para interactuar con el usuario, permitiendo listar, añadir, modificar, buscar y eliminar contactos.

## 📂 Estructura del Proyecto
```plaintext
POO-Objetos/
├── ejercicio-3-diccionario-de-contactos/
│   ├── __pycache__/          # Caché de Python (se genera automáticamente)
│   ├── __init__.py           # Archivo de inicialización
│   ├── Persona.py            # Clase Persona con encapsulamiento y validaciones
│   ├── Principal.py          # Programa principal que gestiona los contactos
│   └── README.md             # Archivo de documentación del ejercicio
```

## 🛠️ Tecnologías Utilizadas
- **Lenguaje**: Python
- **Paradigma:**: programación Orientada a Objetos (POO)
- **Versión de Python:** 3.10 o superior

## 📜 Descripción de los Archivos

### 1. `Persona.py`
Este archivo contiene la clase `Persona`, que encapsula los datos de un contacto: nombre, dirección y teléfono. También incluye validaciones para garantizar que los datos ingresados sean correctos.

#### Métodos Principales:
- **Constructor `__init__`:** Inicializa una instancia con validación de nombre y teléfono.
- **Métodos Getters y Setters:** Acceso y modificación de los atributos encapsulados.
- **Validaciones Privadas:** Métodos para validar que los datos cumplen con los requisitos (por ejemplo, un teléfono de 9 dígitos).
- **Método `__str__`:** Devuelve una representación legible de un objeto `Persona`.

### 2. `Principal.py`
Este archivo contiene el programa principal que interactúa con el usuario a través de un menú de opciones. Utiliza la clase `Persona` para gestionar los contactos.

#### Funcionalidades Implementadas:
- **Listar contactos:** Muestra los contactos almacenados en orden alfabético.
- **Añadir un contacto:** Permite ingresar un nuevo contacto al diccionario.
- **Modificar un contacto:** Actualiza los datos de un contacto existente.
- **Buscar un contacto:** Busca un contacto por su número de teléfono.
- **Eliminar un contacto:** Elimina un contacto por su nombre.
- **Salir:** Finaliza el programa.

### 3. `README.md`
Archivo de documentación del proyecto.

## 🚀 Ejecución del Proyecto

1. Clona este repositorio en tu máquina local.
2. Asegúrate de tener Python 3.10 o superior instalado.
3. Ejecuta el archivo `Principal.py` desde la terminal para iniciar el programa:
   ```bash
   python Principal.py
    ```
4. Sigue las instrucciones en pantalla para interactuar con el programa.

## 👤 Autor
  - **Nombre:** Richard Chadwick Plaza
  - **Curso:** 2ºDAM
  - **Asignatura:** Python