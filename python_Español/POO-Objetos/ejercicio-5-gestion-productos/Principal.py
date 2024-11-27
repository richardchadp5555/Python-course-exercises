# Principal.py
# En este archivo se encuentra la función main(), el archivo principal del programa donde podemos probar su funcionalidad
# Richard Chadwick Plaza

from Electronico import Electronico
from Ropa import Ropa
from Comida import Comida

# Lista para almacenar los productos
productos = []

# Método para mostrar el menú
# Mostrar el menú
def mostrarMenu():
    print("\n************ MENÚ ************")
    print("1. Añadir producto Electrónico")
    print("2. Añadir producto de Ropa")
    print("3. Añadir producto de Comida")
    print("4. Listar productos")
    print("5. Salir")

# Método para añadir un producto Electrónico
def añadirElectronico():
    try:
        nombre = input("Introduce el nombre del producto: ").strip()
        precio = float(input("Introduce el precio del producto: "))
        descuento = int(input("Introduce el descuento (%): "))
        producto = Electronico(nombre, precio, descuento)
        productos.append(producto)
        print(f"Producto electrónico '{nombre}' añadido correctamente.")
    except ValueError as e:
        print(f"Error al añadir el producto: {e}")

# Método para añadir un producto de Ropa
def añadirRopa():
    try:
        nombre = input("Introduce el nombre del producto: ").strip()
        precio = float(input("Introduce el precio del producto: "))
        descuento = int(input("Introduce el descuento (%): "))
        producto = Ropa(nombre, precio, descuento)
        productos.append(producto)
        print(f"Producto de ropa '{nombre}' añadido correctamente.")
    except ValueError as e:
        print(f"Error al añadir el producto: {e}")

# Método para añadir un producto de Comida
def añadirComida():
    try:
        nombre = input("Introduce el nombre del producto: ").strip()
        precio = float(input("Introduce el precio del producto: "))
        descuento = 0  # La comida no permite descuentos
        producto = Comida(nombre, precio, descuento)
        productos.append(producto)
        print(f"Producto de comida '{nombre}' añadido correctamente.")
    except ValueError as e:
        print(f"Error al añadir el producto: {e}")

# Método para listar todos los productos
def listarProductos():
    if not productos:
        print("No hay productos registrados.")
    else:
        print("\n--- Lista de Productos ---")
        for producto in productos:
            print(producto)
            print(f"Precio final: {producto.calcularPrecioFinal()}€")
            print("---------------------------")

# Método principal
def main():
    while True:
        mostrarMenu()
        opcion = input("Selecciona una opción: ").strip()
        match opcion:
            case "1":
                añadirElectronico()
            case "2":
                añadirRopa()
            case "3":
                añadirComida()
            case "4":
                listarProductos()
            case "5":
                print("Saliendo del programa...")
                break
            case _:
                print("La opción introducida no es válida")

# Ejecución del programa 
main()