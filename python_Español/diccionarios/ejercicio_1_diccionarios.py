# ejercicio_1_diccionario.py
# Escribe un programa que lea una cadena y devuelva un diccionario con la cantidad de apariciones de cada caracter en la cadena

# Inicializamos un diccionario vacío
diccionario = {}

# Pedimos la cadena 
cadena = input("Introduce una cadena de texto ")
for caracter in cadena:
    if caracter in diccionario:
        diccionario[caracter] += 1                  # Si está en el diccionario aumentamos en 1 el contador
    else:
        diccionario[caracter] = 1                   # Si no está lo añadimos al diccionario y establecemos su contador er 1

# Mostramos el resultado por pantalla
for campo, valor in diccionario.items():
    print(campo, " - ",valor)
