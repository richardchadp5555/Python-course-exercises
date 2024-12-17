from peewee import Model, AutoField, CharField, FloatField, ForeignKeyField, DateField
from conexionMySQL import ConexionMySQL

conexionMySQL = ConexionMySQL()
db = conexionMySQL.conectar()

class BaseModel(Model):
    class Meta:
        database = db

class Estudiante(BaseModel):
    id = AutoField()
    nombre = CharField(max_length=100)
    correo = CharField(max_length=100, unique=True)

    class Meta:
        table_name = "Estudiantes"

class Curso(BaseModel):
    id = AutoField()
    nombre = CharField(max_length=100)
    precio_mensual = FloatField()  # Aquí corregido: coincide con la base de datos
    descripcion = CharField(max_length=300, null=True)

    class Meta:
        table_name = "Cursos"


class Matricula(BaseModel):
    id = AutoField()
    estudiante = ForeignKeyField(Estudiante, backref='matriculas')
    curso = ForeignKeyField(Curso, backref='matriculas')
    calificacion = FloatField(null=True)
    fecha_matricula = DateField()
    fecha_inicio = DateField()
    fecha_fin = DateField()

    class Meta:
        table_name = "Matriculas"

if __name__ == "__main__":
    try:
        db.create_tables([Estudiante, Curso, Matricula])
        print("Modelos creados exitosamente.")
    except Exception as e:
        print(f"Error al crear los modelos: {e}")
    finally:
        conexionMySQL.cerrar()
