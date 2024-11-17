# ejercicio_5_diccionarios.py
# Se nos pide hacer un analisis de ventas diarias y mensuales de una tienda. Para ello utilizremos un diccionario que contiene las ventas de cada producto para cada día del mes. 
# Nuestro análisis debe incluir la venta total mensual de cada producto, el producto más vendido y el menos vendido de cada mes, las verntas dirarias del producto con mayor venta mensual y el día con mayor cantidad de ventas para cada producto.
# Supongamos que tenemos las ventas de cuatro productos. En este diccionario, las claves principales son los productos y cada clave de producto tiene un diccionarionanidado donde las claves son los días y los valores son las unidades vendidas

# Menú
def verMenu():
    print("ANÁLISIS DE VENTAS")
    print("**********************************************************************************")
    print("1) Calcular el total de unidades vendidas en el mes para cada producto ")
    print("2) Identificar el producto con más y menos ventas en el mes ")
    print("3) Mostrar las ventas diarias del producto más vendido ")
    print("4) Encontrar el día con la mayor venta para cada producto ")
    print("5) Salir")

# Método para calular el total de unidades vendidas en el mes de un producto
def calcularVentas(producto, ventas):
    sumaVentas = 0

    for i in range(30):
        sumaVentas += ventas[producto][str(i + 1)]
    return sumaVentas

# Método para obtener el total de unidades vendidas en el mes de cada producto, devuelve un diccionario con las ventas totales de cada producto
def ventasTotales(ventas):
    ventasMensuales = {}

    for producto in ventas.keys():
        ventasMensuales[producto] = calcularVentas(producto, ventas)
    return ventasMensuales

# Método para determinar el producto más vendido y el menos vendido del mes
def obtenerExtremosVentas(ventasMensuales):
    ventasProductoMasVendido = 0
    productoMasVendido = ""

    # Determinamos el produco mas vendido
    for producto, ventasTotales in ventasMensuales.items():
        if ventasTotales > ventasProductoMasVendido:
            productoMasVendido = producto
            ventasProductoMasVendido  = ventasTotales
    
    # Determinamos el producto menos vendido
    ventasProductoMenosVendido = ventasProductoMasVendido           # Inicializamos en el valor más alto posible
    productoMenosVendido = ""

    for producto, ventasTotales in ventasMensuales.items():
        if ventasTotales < ventasProductoMenosVendido:
            productoMenosVendido = producto
            ventasProductoMenosVendido = ventasTotales

    return (productoMasVendido, ventasProductoMasVendido), (productoMenosVendido, ventasProductoMenosVendido)

# Método para determinar el día con la mayor venta de un producto
def diaMayorVenta(producto, ventas):
    diaMayorVenta = 1
    cantidadMayorVenta = 0

    for dia, unidades in ventas[producto].items():
        if unidades > cantidadMayorVenta:
            diaMayorVenta = dia
            cantidadMayorVenta = unidades
    
    return diaMayorVenta, cantidadMayorVenta
    
# Main
def main():
    continuarProrama = True         # Variable bandera para el bucle

    # Diccionario de ventas de cuatro productos cada día del mes (30 días)
    ventas = {
        "portatil": {
            "1": 5, "2": 7, "3": 10, "4": 8, "5": 12,
            "6": 9, "7": 11, "8": 4, "9": 6, "10": 10,
            "11": 8, "12": 13, "13": 7, "14": 15, "15": 6,
            "16": 9, "17": 12, "18": 10, "19": 8, "20": 7,
            "21": 11, "22": 5, "23": 14, "24": 9, "25": 10,
            "26": 12, "27": 8, "28": 13, "29": 7, "30": 6
        },
        "teclado": {
            "1": 10, "2": 8, "3": 9, "4": 12, "5": 7,
            "6": 10, "7": 6, "8": 8, "9": 11, "10": 9,
            "11": 13, "12": 14, "13": 12, "14": 8, "15": 7,
            "16": 6, "17": 10, "18": 7, "19": 9, "20": 12,
            "21": 14, "22": 13, "23": 6, "24": 8, "25": 7,
            "26": 9, "27": 10, "28": 11, "29": 6, "30": 8
        },
        "mouse": {
            "1": 15, "2": 18, "3": 20, "4": 12, "5": 14,
            "6": 17, "7": 19, "8": 13, "9": 16, "10": 15,
            "11": 18, "12": 14, "13": 17, "14": 20, "15": 19,
            "16": 15, "17": 16, "18": 14, "19": 13, "20": 17,
            "21": 20, "22": 18, "23": 19, "24": 16, "25": 15,
            "26": 18, "27": 20, "28": 17, "29": 14, "30": 19
        },
        "alfombrilla": {
            "1": 8, "2": 7, "3": 6, "4": 10, "5": 9,
            "6": 8, "7": 7, "8": 6, "9": 5, "10": 9,
            "11": 8, "12": 7, "13": 10, "14": 6, "15": 9,
            "16": 8, "17": 7, "18": 6, "19": 10, "20": 8,
            "21": 7, "22": 9, "23": 6, "24": 10, "25": 8,
            "26": 9, "27": 7, "28": 6, "29": 8, "30": 10
        }
    }

    # Bucle para gestionar el menu
    ventasMensuales = ventasTotales(ventas)                        # Obtenemos las ventas totales de cada producto
    (productoMasVendido, ventasProductoMasVendido), (productoMenosVendido, ventasProductoMenosVendido) = obtenerExtremosVentas(ventasMensuales)

    while continuarProrama:
        verMenu()
        opcionMenu = input("Introduce una opción (1 - 5): ")
        print("\n")

        match opcionMenu:
            case "1":  # Mostramos el total de ventas de cada producto en el mes                                        
                for producto, total in ventasMensuales.items():             
                    print(f"{producto}: {total} unidades ")
                    print("\n")
            case "2":  # Mostramos el producto más vendido y el menos vendido  
                print(f"El producto más vendido del mes es {productoMasVendido} con un total de ventas de {ventasProductoMasVendido}")
                print("\n")
                print(f"El producto menos vendido del mes es {productoMenosVendido} con un total de ventas de {ventasProductoMenosVendido}")
                print("\n")
            case "3":  # Mostramos las ventas diarias del producto más vendido
                print(f"El producto más vendido este mes es {productoMasVendido}, sus ventas diarias son: ")
                print("\n")
                for dia, cantidadVentas in ventas[productoMasVendido].items():
                    print(f"Día: {dia} - ventas: {cantidadVentas}")
                    print("\n")
            case "4": # Mostramos las mayores ventas de cada producto
                for producto in ventas.keys():
                    dia, cantidad = diaMayorVenta(producto, ventas)
                    print(f"La mayor venta de {producto} ocurrió el día {dia} con una cantidad de {cantidad} unidades vendidas")
                    print("\n")
            case "5":
                print("Saliendo...")
                print("\n")
                continuarProrama = False
            case _:
                print("Opción introducida no válida. ")

# Ejecutamos el programa
main()
