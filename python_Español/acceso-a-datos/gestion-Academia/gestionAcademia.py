# gestionAcademia.py
# Programa principal para la gestión de la academia
# Autor: Richard Chadwick Plaza
# Lenguaje: Python
# Tecnologías: Peewee
# Asignatura: Acceso a datos

from modelos import Estudiante, Curso, Matricula
from conexionMySQL import ConexionMySQL
import datetime

# Conexión a la base de datos
conexionMySQL = ConexionMySQL()
db = conexionMySQL.conectar()

# Función para listar los cursos disponibles
def listarCursos():
    try:
        cursos = Curso.select()
        print("\n--- Cursos Disponibles ---")
        for curso in cursos:
            print(f"{curso.id}. {curso.nombre}")
    except Exception as e:
        print(f"Error al listar los cursos: {e}")

# Función para listar los estudiantes en un curso
def listarEstudiantesEnCurso():
    try:
        listarCursos()
        nombreCurso = input("Introduce el nombre del curso: ")
        curso = Curso.get_or_none(Curso.nombre == nombreCurso)
        if not curso:
            print(f"Error: No existe un curso con el nombre '{nombreCurso}'.")
            return
        print(f"\n--- Estudiantes Matriculados en '{nombreCurso}' ---")
        matriculas = Matricula.select().where(Matricula.curso == curso)
        if matriculas:
            for matricula in matriculas:
                print(f"Nombre: {matricula.estudiante.nombre}")
        else:
            print("No hay estudiantes matriculados en este curso.")
    except Exception as e:
        print(f"Error: {e}")

# Función para dar de baja a un estudiante en un curso
def darBajaEstudiante():
    try:
        nombreEstudiante = input("Nombre del estudiante: ")
        nombreCurso = input("Nombre del curso: ")
        estudiante = Estudiante.get_or_none(Estudiante.nombre == nombreEstudiante)
        curso = Curso.get_or_none(Curso.nombre == nombreCurso)
        if estudiante and curso:
            matricula = Matricula.get_or_none((Matricula.estudiante == estudiante) & (Matricula.curso == curso))
            if matricula:
                matricula.delete_instance()
                print(f"{nombreEstudiante} fue dado de baja del curso '{nombreCurso}'.")
            else:
                print("El estudiante no está matriculado en ese curso.")
        else:
            print("Estudiante o curso no existen.")
    except Exception as e:
        print(f"Error: {e}")

# Función para actualizar el precio de un curso
def actualizarPrecioCurso():
    try:
        listarCursos()
        nombreCurso = input("Nombre del curso a actualizar: ")
        nuevoPrecio = float(input("Nuevo precio mensual: "))
        curso = Curso.get_or_none(Curso.nombre == nombreCurso)
        if curso:
            curso.precio_mensual = nuevoPrecio
            curso.save()
            print(f"El precio del curso '{nombreCurso}' ha sido actualizado.")
        else:
            print("Curso no encontrado.")
    except ValueError:
        print("Error: Introduce un precio válido.")
    except Exception as e:
        print(f"Error: {e}")

# Función para emitir recibos de un estudiante
def emitirRecibos():
    try:
        nombreEstudiante = input("Nombre del estudiante: ")
        estudiante = Estudiante.get_or_none(Estudiante.nombre == nombreEstudiante)
        if estudiante:
            matriculas = Matricula.select().where(Matricula.estudiante == estudiante)
            if matriculas:
                print(f"\n--- Recibos de '{nombreEstudiante}' ---")
                for matricula in matriculas:
                    print(f"Curso: {matricula.curso.nombre} | Precio: {matricula.curso.precio_mensual}€")
            else:
                print("El estudiante no tiene matrículas registradas.")
        else:
            print("Estudiante no encontrado.")
    except Exception as e:
        print(f"Error: {e}")

# Función para matricular un estudiante
def matricularEstudiante():
    try:
        nombreEstudiante = input("Nombre del estudiante: ")
        listarCursos()
        nombreCurso = input("Nombre del curso: ")
        fechaInicio = input("Fecha de inicio (YYYY-MM-DD): ")
        fechaFin = input("Fecha de fin (YYYY-MM-DD): ")
        fechaMatricula = datetime.date.today()

        estudiante = Estudiante.get_or_none(Estudiante.nombre == nombreEstudiante)
        curso = Curso.get_or_none(Curso.nombre == nombreCurso)
        if estudiante and curso:
            Matricula.create(
                estudiante=estudiante,
                curso=curso,
                calificacion=None,
                fecha_matricula=fechaMatricula,
                fecha_inicio=fechaInicio,
                fecha_fin=fechaFin
            )
            print(f"{nombreEstudiante} matriculado en '{nombreCurso}'.")
        else:
            print("Error: Estudiante o curso no encontrados.")
    except ValueError:
        print("Error: Fechas inválidas.")
    except Exception as e:
        print(f"Error: {e}")

# Función principal
def main():
    while True:
        print("\n--- Gestión de Academia ---")
        print("1. Matricular a un estudiante en un curso")
        print("2. Listado de estudiantes en un curso")
        print("3. Baja de un estudiante en un curso")
        print("4. Actualizar el precio de un curso")
        print("5. Emitir recibos (por estudiante)")
        print("6. Salir")

        try:
            opcion = int(input("Introduce una opción: "))
            match opcion:
                case 1: matricularEstudiante()
                case 2: listarEstudiantesEnCurso()
                case 3: darBajaEstudiante()
                case 4: actualizarPrecioCurso()
                case 5: emitirRecibos()
                case 6: print("Saliendo..."); break
                case _: print("Opción no válida.")
        except ValueError:
            print("Error: Introduce un número válido.")

if __name__ == "__main__":
    main()
