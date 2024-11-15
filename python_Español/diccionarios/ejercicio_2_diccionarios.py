# ejercicio_2_diccionarios.py

# En este programa vamos a declarar un diccionario para los precios de distintas frutas. El programa pedirá el nombre de la fruta y la cantidad que se ha vendido y nos mostrará el precio final de la fruta a partir de los datos guardados en el diccionario. Si la fruta no existe nos drará un error. Tras cada consulta el programa nos preguntará si queremos hacer otra consulta.

# La clave será el nombre de la fruta y el valor será su precio

precios = {"manzana": 2, "naranja": 1.5, "plátano": 4, "piña": 3}
venderFruta = True

while venderFruta:
    fruta = input("Dime la fruta que has vendido: ").lower()
    if fruta not in precios:
        print("Esta fruta no existe en el sistema. ")
    else:
        try:
            cantidad = int(input(f"Dime la cantidad de {fruta} que has vendido: "))
            precioTotal = cantidad * precios[fruta]
            print(f"El precio por esa cantidad de {fruta} es: ", str(precioTotal))
        except ValueError:
            print("Introduce un número válido")

    # Comprobamos si el usuario quiere continuar con el programa
    opcion = input("¿Quieres vender otra fruta? (si / no)")
    while opcion.lower() != "si" and opcion.lower() != "no":
        opcion = input("¿Quieres vender otra fruta? (si / no)")
    if opcion.lower() == "no":
        venderFruta = False
    