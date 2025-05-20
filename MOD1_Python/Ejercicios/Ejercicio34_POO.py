# Ejercicio 34:

# Disena una clase llamada CuentaBancaria con los atributos:
    # titular: nombre del dueno de la cuenta.
    # saldo: comienza en 0 si no se indica lo contrario.

# La clase debe tener los siguientes metodos:
    # depositar(monto): suma el monto al saldo.
    # retirar(monto): resta el monto si hay suficiente saldo; si no, muestra un mensaje de error.
    # mostrar_saldo(): imprime el saldo actual y el nombre del titular.
#---------------------------------------------------------------------------------------------

# Creamos nuestra clase cuenta bancaria

class CuantaBancaria:
    def __init__(self, titular, saldo = 0):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, monto):
        self.saldo += monto
    
    def retirar(self, monto):
        if monto <= self.saldo:
            self.saldo -= monto
        else:
            print("Fondos insuficientes.")

    def mostrar_saldo(self):
        print(f"Saldo actual de {self.titular}: ${self.saldo}")

# Uso 
cuenta = CuantaBancaria("Lucia")

cuenta.mostrar_saldo()
cuenta.depositar(1000)
cuenta.mostrar_saldo()
cuenta.retirar(300)
cuenta.mostrar_saldo()
cuenta.retirar(2000)