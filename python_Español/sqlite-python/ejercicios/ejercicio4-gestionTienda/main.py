# main.py
# en este programa gestionamos la tienda mediante un menú iteractivo
# Autor: Richard Chadwick Plaza
# Curso: Segundo DAM
# Lenguaje: Python

from tienda import Tienda
from producto import Producto

def menu():
    tienda = Tienda('tienda.db')

    while True:
        print("Bienvenido! ¿Qué quieres hacer?")
        print("1. Insertar un producto. ")
        print("2. Consultar los productos de la tienda. ")
        print("3. Actualizar un producto. ")
        print("4. Eliminar un producto. ")
        print("5. Salir. ")
        opcion = input("Introduce una opción: ")

        match opcion:
            case '1':   # Insertar un producto
                try:
                    nombre = input("Introduce el nombre del producto: ")
                    precio = float(input("Introduce el precio del producto: "))
                    stock = int(input("Introduce el stock del producto: "))
                    producto = Producto(None, nombre, precio, stock)
                    tienda.insertar_producto(producto)
                except ValueError:
                    print("ERROR: Asegurate de introducir datos válidos (nombre: cadena de caracteres, precio: numérico, stock: numérico).")

            case '2':   # Consultar los productos
                tienda.consultar_productos()

            case '3':   # Actualizar un producto
                try:
                    id_producto = int(input("Introduce el id del producto a actualizar: "))

                    # Buscamos el producto a partir del id
                    producto_actual = tienda.buscar_producto_por_id(id_producto)

                    if producto_actual:
                        print(f"Has seleccionado el producto: {producto_actual}")
                        confirmar = input("¿Deseas actualizar este producto? (si/no)").strip().lower()
                        if confirmar == 'si':
                            nuevo_nombre = input(f"Introduce el nuevo nombre del producto (actual: {producto_actual.nombre}): ") or producto_actual.nombre
                            nuevo_precio = input(f"Introduce el nuevo precio del producto (actual: {producto_actual.precio}): ")
                            nuevo_precio = float(nuevo_precio) if nuevo_precio else producto_actual.precio
                            nuevo_stock = input(f"Introduce el nuevo stock del producto (actual: {producto_actual.stock}): ")
                            nuevo_stock = int(nuevo_stock) if nuevo_stock else producto_actual.stock
                            tienda.actualizar_producto(id_producto, nuevo_nombre, nuevo_precio, nuevo_stock)
                        elif confirmar == 'no':
                            print("Operación cancelada. ")
                        else:
                            print("No te he entendido. ")
                    else:
                        print("No se ha encontrado ningún producto con ese id en el almacén. ")
                except ValueError:
                    print("ERROR: Asegúrate de introducir un id válido (numérico).")

            case '4':   # Eliminar un producto
                try:
                    id_producto = int(input("Introduce el id del producto que quieres eliminar: "))

                    # Buscamos el producto
                    producto_eliminar = tienda.buscar_producto_por_id(id_producto)
                    
                    if producto_eliminar:
                        print(f"Has seleccionado el producto: {producto_eliminar}")
                        confirmar = input("¿Deseas eliminar este producto? (si/no)").strip().lower()
                        if confirmar == 'si':
                            tienda.eliminar_producto(id_producto)
                        elif confirmar == 'no':
                            print("Operación cancelada")
                        else:
                            print("No te he entendido ")
                    else:
                        print("No se ha encontrado ningún producto con ese id en el almacén. ")
                except ValueError:
                    print("ERROR: Asegúrate de introducir un id válido (numérico)")
            case '5':
                # Salir
                print("Saliendo...")
                tienda.cerrar_conexion()
                break
            case _:
                # Opción no válida
                print("La opción introducida no es válida, introduce un número del 1 al 5. ")

def main():
    menu()

main()