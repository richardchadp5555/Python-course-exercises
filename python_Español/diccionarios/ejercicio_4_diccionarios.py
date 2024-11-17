# ejercicio_4_diccionarios.py

# Este programa pide al usuario su nombre, edad, dirección, y teléfono y lo guarda en un diccionario. Después muestra por pantalla <nombre> tiene <edad> años, vive en <dirección> y su número de teléfono es <teléfono>.

def main():
    nombre = input("Introduce tu nombre: ")
    edad = input("Introduce tu edad: ")
    direccion = input("Introduce tu dirección: ")
    telefono = input("Introduce tu teléfono: ")

    informacionUsuario = {
        "nombre": nombre,
        "edad": edad,
        "direccion": direccion,
        "telefono": telefono 
    }

    print(f"{informacionUsuario['nombre']} tiene {informacionUsuario[edad]} años, vive en {informacionUsuario[direccion]} y su número de teléfono es {informacionUsuario[telefono]}")