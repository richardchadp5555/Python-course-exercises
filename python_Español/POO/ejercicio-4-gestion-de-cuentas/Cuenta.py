# Cuenta.py
# En este archivo creamos una clase Cuenta para gestionar operaciones bancarias.
# La cuenta tiene un titular (de la clase Persona), un saldo inicial, y permite operaciones como ingresar y retirar dinero.
# Autor: Richard Chadwick Plaza         Curso: 2ºDAM        Python

from Persona import Persona     # Importamos la clase Persona

class Cuenta:
    def __init__(self, titular = None, saldo = 0):
        self.setTitular(titular)
        self.__saldo = saldo            # Inicializamos directamente el saldo sin setters
        
    # GETTERS
    def getTitular(self):
        return self.__titular
    
    def getSaldo(self):
        return self.__saldo
    
    # SETTERS
    def setTitular(self, titularNuevo):
        if not isinstance(titularNuevo, Persona):
            raise ValueError("Error: El titular debe ser una instancia de la clase Persona")
        self.__titular = titularNuevo
    
    # No hay setter para el saldo, para modificar el saldo hay que usar los métodos ingresar() o retirar()
    
    # Metodos para operar con el saldo
    def ingresar(self, cantidad):
        if not isinstance(cantidad, (int, float)) or cantidad <= 0:
            raise ValueError("Error: La cantidad a ingresar debe ser un número entero positivo")
        self.__saldo += cantidad
    
    def retirar(self, cantidad):
        if not isinstance(cantidad, (int, float)) or cantidad <= 0:
            raise ValueError("Error: La cantidad a retirar debe ser un número entero positivo")
        self.__saldo -= cantidad        # Se permite que el saldo quede en rojo si la cantidad a retirar supera los fondos

    # Método mostrar() que muestra todos los datos de la cuenta
    def mostrar(self):
        return f"- Información del titular: {self.getTitular().mostrar()}\n- Saldo de la cuenta: {self.getSaldo()}"