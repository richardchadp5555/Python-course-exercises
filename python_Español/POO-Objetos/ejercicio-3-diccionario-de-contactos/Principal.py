# Principal.py
# Programa principal para gestionar un diccionario de contactos usando la clase Persona.
# Incluye funcionalidades para listar, añadir, modificar, buscar y eliminar contactos.
#
# Requiere: Persona.py
#
# Autor: Richard Chadwick Plaza      Curso: 2ºDAM      Python

#Importamos la clase Persona
from Persona import Persona

# Diccionario de contactos
contactos = {}

# Método para mostrar el menú
def mostrarMenu():
    print("\n****************MENÚ****************\n")
    print("Introduce una de las opciones siguientes: ")
    print("a) Listado de los contactos por orden alfabético")
    print("b) Añadir un nuevo contacto")
    print("c) Modificar un contacto")
    print("d) Buscar un número de teléfono")
    print("e) Eliminar un contacto")
    print("f) Salir")

# Método para perdir los datos del contacto
def pedirDatos():
    nombre = input("Introduce el nombre del contacto: (Este campo no puede estar vacío)").strip().upper()
    # Comprobamos que el nombre no esté vacío
    while not nombre:
        print("El nombre no puede ser un campo vacío. ")
        nombre = input("Vuelve a introducir el nombre del contacto, recuerda que no puede ser un campo vacíó").strip().upper()
    
    direccion = input("Introduce la dirección del contacto: ")
  
    telefono = input("Introduce el teléfono del contacto: (Este tiene que ser un número de 9 dígitos)").strip()
    # Comprobamos que el teléfono es un número de 9 dígitos 
    while not telefono.isdigit() or len(telefono) != 9:
        print("El teléfono debe ser un número de 9 dígitos, por ejemplo: 123456789")
        telefono = input("Vuelve a introducir el teléfono: ")
    
    return nombre, direccion, telefono

# Método para buscar si un contacto ya existe, si es el caso devuelve True si no False
def existeContacto(nombre):
    return nombre in contactos

# Método para mostrar el listado de contactos ordenados alfabéticamente (si hay contactos en el diccionario)
def listarContactos():
    if contactos:
        for nombre, persona in sorted(contactos.items()):  # Ordenamos por nombre
            print(persona)
    else:
        print("No hay contactos guardados ")
    # Metemos una pausa para seguir
    input("Presiona Enter para continuar...")

# Método para modificar un contacto
def modificarContacto():
    nombre = input("Introduce el nombre del contacto que quieres modificar: ").strip().upper()
    if existeContacto(nombre):
        direccion, telefono = pedirDatos()[1:]
        try:
            contactos[nombre].setDireccion(direccion)
            contactos[nombre].setTelefono(telefono)
            print("Contacto actualizado correctamente ")
        except ValueError as e:
            print(f"Error al modificar el contacto: {e}")
    else:
        print(f"No se ha encontrado ningún contacto con el nombre {nombre}")
    input("Presiona Enter para continuar...")

# Método para añadir un nuevo contacto
def nuevoContacto():
    # Obtenemos los datos del nuevo contacto
    nombre, direccion, telefono = pedirDatos()
    # Si ya existe un contacto con ese nombre:
    if existeContacto(nombre):
        print("Ya existe un contacto con este nombre: ", nombre)
        actualizar = input("¿Quieres actualizar la información del contacto? (s/n)").strip().lower()
        modificarContacto(nombre, direccion, telefono)    
    # Si aún no existe un contacto con ese nombre:
    else:
        try:
            contactos[nombre] = Persona(nombre, direccion, telefono)
            print("Nuevo contacto añadido correctamente. ")
        except ValueError as e:
            print("Error al añadir el nuevo contacto: {e}")           
    input("Presiona Enter para continuar...")

# Método para buscar la información de un contacto por su teléfono
def buscarContacto(): 
    telefono = input("Introduce el teléfono (Este debe ser un número de 9 dígitos): ")
    for persona in contactos.values():
        if persona.getTelefono() == telefono:
            print(f"Contacto encontrado, el teléfono pertenece a {persona.getNombre()}")
            verContacto = input("¿Quieres ver toda la información del contacto? (s/n):").strip().lower()
            if verContacto == "s":
                print(persona)
            input("Presiona Enter para continuar...")
            return       # Cortamnos el programa para que no tenga que recorrer todo el diccionario

    print("No se encontró ningún contacto con ese número de teléfono. ")
    input("Presiona Enter para continuar...")

# Método para eliminar un contacto
def eliminarContacto():
    nombre = input("Introduce el nombre del contacto que quieres eliminar (Recuerda que no puede ser un campo vacío): ").strip().upper()
    if existeContacto(nombre):
        del contactos[nombre]
        print(f"El contacto '{nombre}' ha sido elimninado correctamente")
    else:
        print(f"No se ha encontrado ningún contacto con el nombre '{nombre}")
    input("Presiona Enter para continuar...")



# Main
def main():
    while True:
        mostrarMenu()
        opcion = input("Introduce una opción: ").strip().lower()

        match opcion:
            case "a":
                listarContactos()
            case "b":
                nuevoContacto()
            case "c":
                modificarContacto()
            case "d":
                buscarContacto()
            case "e":
                eliminarContacto()
            case "f":
                print("Saliendo...")
                break       # Salimos del programa
            case _:
                print("Opción no válida")

# Llamada al main
main()