# Principal.py
# Programa principal para gestionar cuentas normales y cuentas jóvenes.
# Utiliza las clases Persona, Cuenta y CuentaJoven.
# Funcionalidades:
#   - Menú de opciones
#   - Gestión de cuentas en un diccionario que usa el DNI como clave para identificar de forma única cada cuenta
#   - Manejo de excepciones
# Autor: Richard Chadwick Plaza         Curso: 2ºDAM        Python

from Persona import Persona       # Importamos la clase Persona
from Cuenta import Cuenta         # Importamos la clase Cuenta
from CuentaJoven import CuentaJoven  # Importamos la clase CuentaJoven

# Diccionario para guardar las cuentas
cuentas = {}    # Clave: DNI, Valor: Objeto de Cuenta o CuentaJoven

# Método para mostrar el menú
def mostrarMenu():
    print("\n************ MENÚ ************")
    print("Introduce una opción (1 - 8): ")
    print("1. Crear una cuenta normal.")
    print("2. Crear una cuenta joven.")
    print("3. Listar todas las cuentas.")
    print("4. Mostrar los detalles de una cuenta.")
    print("5. Ingresar dinero.")
    print("6. Retirar dinero.")
    print("7. Eliminar una cuenta.")
    print("8. Salir.")
    return input("Selecciona una opción: ").strip()

# Método para crear una cuenta normal
def crearCuentaNormal():
    try:
        print("\n--------- CUENTA NORMAL ---------")
        nombre = input("Introduce el nombre del titular de la cuenta: ").strip()
        apellidos = input("Introduce los apellidos del titular de la cuenta: ").strip()
        dni = input("Introduce el DNI del titular: ").strip().upper()
        edad = int(input("Introduce la edad del titular: "))
        saldo = 0.0  # Inicialmente el saldo es 0 hasta que se ingrese dinero

        # Crear objeto Persona
        titular = Persona(nombre, apellidos, dni, edad)
        # Crear cuenta
        cuenta = Cuenta(titular, saldo)
        # Guardar la cuenta en el diccionario
        cuentas[dni] = cuenta
        print("Cuenta normal creada con éxito.")
    except ValueError as e:
        print(f"Error al crear la cuenta: {e}")

# Método para crear una Cuenta Joven
def crearCuentaJoven():
    try:
        print("\n--------- CUENTA JOVEN ---------")
        nombre = input("Introduce el nombre del titular de la cuenta: ").strip()
        apellidos = input("Introduce los apellidos del titular de la cuenta: ").strip()
        dni = input("Introduce el DNI del titular: ").strip().upper()
        edadIntroducida = int(input("Introduce la edad del titular: "))
        if edadIntroducida > 24:
            print("Para crear una cuenta Joven debes tener como máximo 24 años. ")
            return
        else:
            edad = edadIntroducida
        saldo = 0.0  # Inicialmente el saldo es 0 hasta que se ingrese dinero
        bonificacion = float(input("Introduce la bonificación anual de la cuenta (%): "))

        # Crear objeto Persona
        titular = Persona(nombre, apellidos, dni, edad)

        # Crear cuenta joven
        cuentaJoven = CuentaJoven(titular, saldo, bonificacion)

        # Guardar la cuenta en el diccionario
        cuentas[dni] = cuentaJoven
        print("Cuenta joven creada con éxito.")
    except ValueError as e:
        print(f"Error al crear la cuenta joven: {e}")

# Método para listar las cuentas
def listarCuentas():
    if not cuentas:
        print("No hay cuentas registradas.")
    else:
        print("\n--- Listado de Cuentas ---")
        for dni, cuenta in cuentas.items():
            print(f"DNI del titular: {dni} -> {cuenta.mostrar()}")

# Método para mostrar los detalles de una cuenta
def mostrarCuenta():
    try:
        dni = input("Introduce el DNI del titular de la cuenta que quieres consultar: ").strip().upper()
        if dni not in cuentas:
            print("No se encontró ninguna cuenta con ese DNI.")
            return
        print(f"Detalles de la cuenta: {cuentas[dni].mostrar()}")
    except ValueError as e:
        print(f"Error al mostrar los detalles de la cuenta: {e}")

# Método para ingresar dinero
def ingresarDinero():
    try:
        dni = input("Introduce el DNI del titular de la cuenta: ").strip().upper()
        if dni not in cuentas:
            print("No se encontró ninguna cuenta con ese DNI.")
            return
        cantidad = float(input("Introduce la cantidad que quieres ingresar: "))
        if cantidad <= 0:
            print("La cantidad debe ser un número positivo.")
            return
        cuentas[dni].ingresar(cantidad)
        print(f"Se han ingresado {cantidad}€ en la cuenta con DNI {dni}.")
    except ValueError as e:
        print(f"Error al ingresar dinero: {e}")

# Método para retirar dinero
def retirarDinero():
    try:
        dni = input("Introduce el DNI del titular de la cuenta: ").strip().upper()
        if dni not in cuentas:
            print("No se encontró ninguna cuenta con ese DNI.")
            return
        cantidad = float(input("Introduce la cantidad que quieres retirar: "))
        if cantidad <= 0:
            print("La cantidad debe ser un número positivo.")
            return
        cuentas[dni].retirar(cantidad)
        print(f"Se han retirado {cantidad}€ de la cuenta con DNI {dni}.")
    except ValueError as e:
        print(f"Error al retirar dinero: {e}")

# Método para eliminar una cuenta
def eliminarCuenta():
    try:
        dni = input("Introduce el DNI del titular de la cuenta que quieres eliminar: ").strip().upper()
        if dni not in cuentas:
            print("No se encontró ninguna cuenta asociada a ese DNI.")
            return
        del cuentas[dni]
        print("Se ha eliminado correctamente la cuenta.")
    except ValueError as e:
        print(f"Error al eliminar la cuenta: {e}")

# Definición de main
def main():
    while True:
        opcion = mostrarMenu()
        match opcion:
            case "1":
                crearCuentaNormal()
            case "2":
                crearCuentaJoven()
            case "3":
                listarCuentas()
            case "4":
                mostrarCuenta()
            case "5":
                ingresarDinero()
            case "6":
                retirarDinero()
            case "7":
                eliminarCuenta()
            case "8":
                print("Saliendo...")
                break  # Cerramos el programa
            case _:
                print("La opción introducida no es válida.")

# Llamamos a main
main()
