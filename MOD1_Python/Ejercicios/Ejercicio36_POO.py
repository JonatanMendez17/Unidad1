# Ejercicio 36:

# Crear una clase Termometro con un atributo temperatura y un metodo:
    # indicar_estado() que indique si la temperatura esta en estado "frio" (menos de 15°), "templado" (15 a 25°) o "calor" (mas de 25°). 
    # Crear distintos termometros y mostrar su estado.

class Termometro:
    def __init__(self, temperatura):
        self.temperatura = temperatura

    def indicar_estado(self):
        if self.temperatura < 15:
            print("Hace frio")
        elif self.temperatura <= 25:
            print("Esta templado")
        else:
            print("Hace calor")

t1 = Termometro(10)
t2 = Termometro(20)
t3 = Termometro(30)

t1.indicar_estado()
t2.indicar_estado()
t3.indicar_estado()
