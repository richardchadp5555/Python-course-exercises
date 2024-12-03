# Principal.py
# En este archivo se encuentra la función main y es donde se concentra y ejecuta la funcionalidad del programa
# Richard Chadwick Plaza

from Material import Material
from Revista import Revista
from Libro import Libro


#Diccionario de materiales
materiales = {}

# Lista de meses
meses = ["enero", "febrero", "marzo", "abril", "mayo", "junio", "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"]

# Generos
generos = ["ficción", "no ficción", "terror", "ciencia"]

# Método para agregar una revista
def agregarRevista():
    id = int(input("Introduce el id de la revista"))
    titulo = input("Introduce el título de la revista, no puede ser un campo vacíó.").strip().lower()
    while not titulo:
        titulo = input("El título no puede ser un campo vacío, vuelve a introducir el título. ")
    
    autor = input("Introduce el autor: ").strip().lower()
    while not autor:
        autor = ("El autor no puede ser un campo vacío, si no tiene autor escribe 'Anónimo'. Vuelve a introducir el autor")
    
    anioPublicacion = int(input("Introduce el año de publicación, recuerda que debe ser un entero positivo: "))
    while not isinstance(anioPublicacion, int) or anioPublicacion < 0:
        anioPublicacion = input("El año de publicación debe ser un entero positivo, vuelve a escribir el año de publicación. ")

    numEdicion = int(input("Introduce el número de edición, recuerda que debe ser un entero positivo: "))
    while not isinstance(numEdicion, int) or numEdicion < 0:
        numEdicion = input("El número de edición debe ser un entero positivo, vuelve a escribir el número de edición. ")

    mesPublicacion = input("Introduce el mes de publicación, recuerda introducir un mes válido ").strip().lower()
    while mesPublicacion not in meses:
        mesPublicacion = input("El mes de publicación de la revista tiene que ser un mes del año real. Vuelve a introducirlo. ").strip().lower()

    try:
        # Aumento en 1 el id para asegurarme q es un id autoincrementado único para cada uno
        revistaNueva = Revista(id, titulo, autor, anioPublicacion, numEdicion, mesPublicacion)
        materiales[id] = revistaNueva
    except ValueError as e:
        # Si hay error volvemos al id anterior para que no hayan incoherencias luego
        contadorId = contadorId - 1
        print(f"Error al crear la revista y agregarla al diccionario")

# Método para generar un Libro
def agregarLibro():
    id = int(input("Introduce el id del libro"))
    titulo = input("Introduce el título del libro, no puede ser un campo vacíó: ").strip().lower()
    while not titulo:
        titulo = input("El título no puede ser un campo vacío, vuelve a introducir el título: ")
    
    autor = input("Introduce el autor: ").strip().lower()
    while not autor:
        autor = ("El autor no puede ser un campo vacío, si no tiene autor escribe 'Anónimo'. Vuelve a introducir el autor")
    
    anioPublicacion = int(input("Introduce el año de publicación, recuerda que debe ser un entero positivo: "))
    while not isinstance(anioPublicacion, int) or anioPublicacion < 0:
        anioPublicacion = input("El año de publicación debe ser un entero positivo, vuelve a escribir el año de publicación. ")

    numEdicion = int(input("Introduce el número de edición, recuerda que debe ser un entero positivo: "))
    while not isinstance(numEdicion, int) or numEdicion < 0:
        numEdicion = input("El número de edición debe ser un entero positivo, vuelve a escribir el número de edición. ")

    genero = input("Introduce el genero, recuerda introducir un genero de entre 'ficción', 'no ficción', 'terror' y 'ciencia' ").strip().lower()
    while genero not in generos:
        genero = input("Introduce el género de nuevo, recuerda que debe estar entre 'ficción', 'no ficción', 'terror' y 'ciencia' ").strip().lower()

    numPaginas = int(input("Introduce el número de páginas: "))
    while numPaginas < 0:
        numPaginas = int(input("Recuerda que el número de páginas debe ser un entero positivo, vuelve a introducir el número de páginas: "))

    try:
        libroNuevo = Libro(id, titulo, autor, anioPublicacion, numEdicion, genero, numPaginas)
        materiales[id] = libroNuevo
    except ValueError as e:
        # Si hay error volvemos al id anterior para que no hayan incoherencias luego
        id -= 1
        print(f"Error al crear la revista y agregarla al diccionario")

# Método para controlar si ya existe un material con un id en el diccionario
def existeMaterial(id):
    return id in materiales

# Método para listar los libros y revistas
def listarMateriales():
    # Controlo que hayan ya guardados
    if materiales:
        for id, material in materiales.items():
            print(material.mostrar())
    else:
        print("No hay material guardado. ")
    input("Presiona Enter para continuar...")

# Método para buscar materiales en función de su id
def BuscarMaterial():
    id = input("Introduce el id del material")
    for material in materiales.values():
        if material.getId() == id:
            print(f"Se ha encontrado el material, su título es {material.getTitulo()}")
            verMaterial = input("¿Quieres ver toda la informacióN del material? (s/n)").strip().lower()
            if verMaterial == "s":
                print(material.mostrar())
            input("Presiona enter para continuar...")
            return  # Corto el bucle para que no tenga que recorrer todo el diccionario
    # Si no se encuentra
    print("No se encontró ningúN material con ese id. ")
    input("Presiona enter para continuar...")

# Método para generar estadísticas
def generarEstadisticas():
    numeroLibros = 0
    numeroRevistas = 0
    totalpaginasLibros = 0
    for material in materiales.values():
        if isinstance(material, Libro):
            numeroLibros += 1
            totalpaginasLibros += material.getNumPaginas()
        if isinstance(material, Revista):
            numeroRevistas += 1
    promedioPaginasLibros = totalpaginasLibros / numeroLibros
    totalMaterial = numeroLibros + numeroRevistas
    print(f"El total de revistas es: {numeroRevistas}, el total de libros es {numeroLibros}, el número total de material almacenado es: {totalMaterial}, el promedio de páginas de libros es {promedioPaginasLibros}")
    
# Método para ver el menú
def verMenu():
    print("---------- MENÚ ----------")
    print("1. Agregar nuevo material. ")
    print("2. Listar materiales. ")
    print("3. Buscar material a partir de su id. ")
    print("4. Eliminar material ")
    print("5. Generar estadísticas. ")
    print("6. Salir. " )

# Main
def main():
    while True:
        verMenu()
        opcion = int(input("Introduce una opción (1 - 6)"))
        match opcion:
            case 1:
                seleccion = input("Introduce a para agrear una revista, introduce b para agregar un libro, introduce c para salir")
                match seleccion:
                    case "a":
                        agregarRevista()
                    case "b":
                        agregarLibro()
                    case "c":
                        return
                    case _:
                        print("Opción no válida. ")
            case 2:
                listarMateriales()
            case 3:
                BuscarMaterial()
            #case 4:
            case 5:
                generarEstadisticas()
            case 6:
                print("Saliendo...")
                break   # Salimos
            case _:
                print("Opción no válida")

# EjecucióN
main()