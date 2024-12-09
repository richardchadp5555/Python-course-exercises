# DNI.py

# Vamos a crear la clase DNI donde vamos a guardar el número de DNI
# (Lo vamos a guardar en una cadena de longitud 8) y la letra correspondiente.
# Vamos a crear el constructor que recibe el número del DNI y automáticamente genera la letra
# Crearemos también los métodos getters y setters
# Se debe definir el método mostrar() para imprimir el DNI

# Autor: Richard Chadwick Plaza        Curso: 2ºDAM        Python

class DNI():
    def __init__(self, numero):
        if not isinstance(numero, str) or len(numero) != 8 or not numero.isdigit():
            raise ValueError("El número debe ser una cadena de 8 dígitos.")
        self.numero = numero
        self.letra = self.__calcularLetra(self)
    
    # Método para calcular la letra
    def __calcularLetra(self):
        letras = 'TRWAGMYFPDXBNJZSQVHLCKE'
        return letras[int(self.numero % 23)]
    
    # Getters
    def getNumero(self):
        return self.numero
    
    def getLetra(self):
        return self.letra

    # Setters
    def setNumero(self, numeroNuevo):
        if not isinstance(numeroNuevo, str) or len(numeroNuevo) != 8 or not numeroNuevo.isdigit():
            raise ValueError("El número debe ser una cadena de 8 dígitos. ")
        self.numero = numeroNuevo
        self.letra = self.__calcularLetra()
    
    # El setter de la letra lo he obviado porque no tiene sentido acceder y modificar la letra, ya que provocaria un error en el formato del dni
    

    # Método mostrar()
    def mostrar(self)
    return f"{self.numero} - {self.letra}"