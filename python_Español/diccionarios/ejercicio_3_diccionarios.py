# ejercicio_3_diccionarios.py
# Este  programa utiliza un diccionario para crear un listín telefónico. El diccionario estará formado por pares nombre - teléfono

import re  # Módulo para expresiones regulares

# Método para mostrar el menú
def verMenu():
    print("\nLISTÍN TELEFÓNICO")
    print("**************************************************************")
    print("a) Listado de teléfonos, usando el orden por defecto")
    print("b) Listado de teléfonos, ordenados alfabéticamente")
    print("c) Añadir un nuevo contacto")
    print("d) Modificar el teléfono de un contacto")
    print("e) Buscar un número de teléfono")
    print("f) Eliminar un contacto")
    print("g) Borrar el listín telefónico")
    print("h) Salir\n")

# Método para validar números de teléfono
def esTelefonoValido(telefono):
    patron = r"^\d{9}$"
    return bool(re.fullmatch(patron, telefono))

# Método para modificar el teléfono de un contacto
def modificarTelefono(nombre, listinTelefonico):
    while True:
        telefonoNuevo = input("Introduce el nuevo teléfono: ").strip()
        if esTelefonoValido(telefonoNuevo):
            listinTelefonico[nombre] = telefonoNuevo
            print(f"Teléfono de {nombre.capitalize()} actualizado correctamente.\n")
            break
        else:
            print("Teléfono no válido. Debe ser un número de 9 dígitos.\n")

# Método para agregar un nuevo contacto
def agregarContacto(nombre, listinTelefonico):
    if nombre in listinTelefonico:
        print(f"Ya existe un contacto con el nombre '{nombre.capitalize()}'")
        actualizarTelefono = input("¿Quieres actualizar su teléfono? (si / no): ").strip().lower()
        if actualizarTelefono == "si":
            modificarTelefono(nombre, listinTelefonico)
    else:
        telefono = input("Introduce el número de teléfono: ").strip()
        if esTelefonoValido(telefono):
            listinTelefonico[nombre] = telefono
            print(f"Contacto {nombre.capitalize()} añadido correctamente.\n")
        else:
            print("Número introducido no válido. Debe ser un número de 9 dígitos.\n")

# Función principal
def main():
    # Listín telefónico precargado
    listinTelefonico = {
        "juan": "123456789",
        "maria": "987654321",
        "pedro": "456789123",
        "ana": "789123456",
        "carlos": "321654987"
    }

    # Variable para gestionar el bucle
    continuar = True

    # Bucle principal
    while continuar:
        verMenu()
        opcionMenu = input("Introduce una opción (a - h): ").strip().lower()

        match opcionMenu:
            case "a":  # Listado por defecto
                print("\nListado de contactos:")
                for nombre, telefono in listinTelefonico.items():
                    print(f"{nombre.capitalize()} - {telefono}")
                print()
            case "b":  # Listado alfabético
                print("\nListado de contactos (orden alfabético):")
                for nombre, telefono in sorted(listinTelefonico.items()):
                    print(f"{nombre.capitalize()} - {telefono}")
                print()
            case "c":  # Añadir un nuevo contacto
                nombre = input("Introduce el nombre del nuevo contacto: ").strip().lower()
                agregarContacto(nombre, listinTelefonico)
            case "d":  # Modificar teléfono
                nombre = input("Introduce el nombre del contacto: ").strip().lower()
                if nombre not in listinTelefonico:
                    respuesta = input("Este nombre no figura en el sistema. ¿Quieres agregarlo? (si / no): ").strip().lower()
                    if respuesta == "si":
                        agregarContacto(nombre, listinTelefonico)
                else:
                    modificarTelefono(nombre, listinTelefonico)
            case "e":  # Buscar un número de teléfono
                nombre = input("Introduce el nombre del contacto cuyo teléfono quieres consultar: ").strip().lower()
                if nombre in listinTelefonico:
                    print(f"\nEl teléfono de {nombre.capitalize()} es {listinTelefonico[nombre]}\n")
                else:
                    print("\nEse nombre no figura en el sistema.\n")
            case "f":  # Eliminar contacto
                nombre = input("Introduce el nombre del contacto que quieres eliminar: ").strip().lower()
                if nombre in listinTelefonico:
                    del listinTelefonico[nombre]
                    print(f"\nContacto {nombre.capitalize()} eliminado.\n")
                else:
                    print("\nEse nombre no figura en el sistema.\n")
            case "g":  # Borrar todo el listín telefónico
                confirmacion = input("¿Estás seguro de que quieres borrar todo el listín? (si / no): ").strip().lower()
                if confirmacion == "si":
                    listinTelefonico.clear()
                    print("\nListín borrado.\n")
            case "h":  # Salir
                print("\nSaliendo...\n")
                continuar = False
            case _:
                print("\nLa opción introducida no existe.\n")

# Ejecutar el programa
main()
