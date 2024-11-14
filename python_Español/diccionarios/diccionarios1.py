# Los diccionarios son un tipo de 'mapa' que nos permiten guardar un conjunto de datos de distinto tipo a los que podemos acceder por medio de una clave, que normalmente es una cadena de caracteres, pero que también puede ser un número.

# Pares clave - valor

# Los diccionarios son un tipo de datos mutable y, además, dentro de los diccionarios, los distintos pares clave-valor que guardamos no están ordenados.


# Creando un diccionario
diccionario = {"uno": 1, "dos": 2, "tres": 3}

# Podemos ver el tipo del diccionario
print(type(diccionario))                    # Salida: <class 'dict'>

# Para acceder a un valor completo ponemos entre corchetes la clave a la que queremos acceder
print(diccionario["dos"])

# También podemos crear diccionarios a partir de uno ya vacío, pudiendole añadir elementos clave-valor nuevos
diccionario2 = {}
diccionario2["nombre"] = "jose"
diccionario2["edad"] = 20
print(diccionario2)

# Operaciones básicas
len(diccionario2)                # Devuelve el tamaño del diccionario
del diccionario["uno"]           # Borra el elemento del diccionario

print("Despues de borrar el elemento 'uno' del primer diccionario: ", diccionario)

# También podemos comprobar si una clave determinada está en el diccionario
print("nombre" in diccionario2)

# Podemos cambiar un elemento del diccionario
diccionario2["nombre"] = "Maria"

print("El segundo diccionario después de cambiar el nombre: ", diccionario2)

# Podriamos copiar un diccionario en otro usando el método copy()
diccionario2 = diccionario.copy()
print("Diccionario2 ", diccionario2)
print("Diccionario ", diccionario)