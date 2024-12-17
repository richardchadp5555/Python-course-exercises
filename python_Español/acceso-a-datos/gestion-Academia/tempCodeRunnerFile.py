# conexionMySQL.py
# En este programa se establece la conexión con la base de datos MySQL en Oracle Cloud Infrastructure para llevar a cabo la gestión de la academia
# Autor: Richard Chadwick Plaza
# Lenguaje: Python
# Tecnologías: Peewee
# Asigantura: Acceso a datos

from peewee import MySQLDatabase

# Configuración de la conexión
db = MySQLDatabase(
    'AcademiaDB',
    user = 'richard',
    password = '(Janadama2024)',
    host = '158.179.221.250',
    port = 3306

)

# Probar la conexión
try:
    db.connect()
    print("Conexión exitosa a MySQL!")
except Exception as e:
    print(f"Error al conectar a la base de datos: {e}")
finally:
    if not db.is_closed():
        db.close()
        print("Conexión cerrada. ")