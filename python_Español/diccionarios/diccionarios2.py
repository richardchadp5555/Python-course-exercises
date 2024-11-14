# diccionarios2.py
# En este ejercicio probaremos algunos de los métodos más importantes a la hora de trabajar con diccionarios

diccionario1 = {"uno": 1, "dos": 2, "tres": 3}

# Método para borrar todos los datos almacenados en un diccionario
diccionario1.clear()
print(diccionario1)         

diccionario1 = {"uno": 1, "dos": 2, "tres": 3}
diccionario2 = {}

# Método para copiar un diccionario en otro
diccionario2 = diccionario1.copy()
print(diccionario2)

# También podemos añadirle la información guardada en un diccionario a otro diccionario
diccionarioNuevo = {}
diccionarioNuevo.update(diccionario2)
print(diccionarioNuevo)

diccionario3 = {"cuatro": 4, "cinco": 5, "seis": 6}
diccionarioNuevo.update(diccionario3)
print(diccionarioNuevo)

# Podemos acceder a una clave guardada en el diccionario usando el método get(), usar esté método puede prevenir excepciones que podemos obtener accediendo de forma corriente diccionario[clave]
print(diccionarioNuevo.get("cuatro"))

print("Probamos a buscar una clave que no esté en el diccionario: ", diccionarioNuevo.get("diez"))

# El método get() también permite definir el valor que devuelve el método cuando no exista la clave
print("Probamos de nuevo una clave que no exista: ", diccionarioNuevo.get("doce", "No existe"))

# El método pop() nos devuelve el método indicado y lo elimina
diccionarioNuevo.pop("uno")
print(diccionarioNuevo)

# Este método también permite asignar valores por defecto para cuando no exista la clave
print(diccionarioNuevo.pop("uno", "No existe"))

# Los diciconarios se pueden recorrer de tres formas: podemos recorrer las claves, los valores o las claves y valores
# Recorremos las claves
print("Las claves: ")
for clave in diccionarioNuevo.keys():
    print(clave)

# Recorremos los valores
print("Los valores ")
for valor in diccionarioNuevo.values():
    print(valor)

# Recorremos las clave-valor
print("Los pares clave-valor: ")
for clave, valor in diccionarioNuevo.items():
    print(clave, valor)