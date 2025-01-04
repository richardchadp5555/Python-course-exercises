# CuentaJoven.py
# En este archivo creamos la clase CuentaJoven, que hereda de Cuenta.
# La clase está diseñada para clientes menores de 25 años y añade el atributo bonificación.
# Autor: Richard Chadwick Plaza         Curso: 2ºDAM        Python

from Cuenta import Cuenta           # Importamos la clase Cuenta que es la clase padre de CuentaJoven

class CuentaJoven(Cuenta):
    def __init__(self, titular, saldo = 0, bonificacion = 0):
        # Controlamos que el titular tenga menos de 25 años
        if titular.getEdad() >= 25:
            raise ValueError("Error: el titular debe ser menor de 25 años para abrir una Cuenta Joven")
        super().__init__(titular, saldo)        # Inicializamos los atributos de la clase Padre
        self.setBonificacion(bonificacion)

    # Getter
    def getBonificacion(self):
        return self.__bonificacion
    
    # Setter
    def setBonificacion(self, bonificacionNueva):
        if not isinstance(bonificacionNueva, (int, float)) or not (0 <= bonificacionNueva <= 100):
            raise ValueError("La bonificación debe ser un porcentaje entre 0 y 100")
        self.__bonificacion = bonificacionNueva
    
    # Método para calcular y aplicar la bonificación al saldo
    def aplicarBonificacion(self):
        beneficio = self.getSaldo() * (self.getBonificacion() / 100)
        self.ingresar(beneficio)
    
    # Método mostrar() adaptado para CuentaJoven
    def mostrar(self):
        return "\nCuenta Joven: \n" + super().mostrar() + f"\n- Bonificacion: {self.getBonificacion()} %"