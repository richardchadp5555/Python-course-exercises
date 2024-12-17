from modelos import Estudiante, Curso, Matricula
from conexionMySQL import ConexionMySQL
import datetime

conexion = ConexionMySQL()
db = conexion.conectar()

def insertarDatosPrueba():
    try:
        estudiante1 = Estudiante.create(nombre="Pedro Sanchez", correo="pedroSanchez@gmail.com")
        estudiante2 = Estudiante.create(nombre="Mariano Rajoy", correo="marianoRajoy@gmail.com")

        curso1 = Curso.create(
            nombre="Matemáticas",
            precio_mensual=100.00,
            descripcion="Curso avanzado de álgebra y análisis matemático"
        )
        curso2 = Curso.create(
            nombre="Física",
            precio_mensual=120.50,
            descripcion="Curso de fundamentos de física"
        )

        Matricula.create(
            estudiante=estudiante1,
            curso=curso1,
            calificacion=5,
            fecha_matricula=datetime.date.today(),
            fecha_inicio=datetime.date(2024, 6, 15),
            fecha_fin=datetime.date(2024, 12, 15)
        )
        print("Datos de prueba insertados correctamente.")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        if not db.is_closed():
            db.close()
            print("Conexión cerrada.")

if __name__ == "__main__":
    insertarDatosPrueba()
