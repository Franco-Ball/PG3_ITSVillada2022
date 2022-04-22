# --------------------- CLASE PERSONA ---------------------#
class Persona:
    def __init__(self):
        self.name = input("Ingrese el nombre de la persona: ")
        self.age = input("Ingrese la edad de la persona: ")

    def imprimir(self):
        print(f"Nombre : {self.name}")
        print(f"Edad : {self.age}")


# --------------------- CALSE EMPLEADO ---------------------#
class Empleado(Persona):
    def __init__(self):
        super().__init__()
        self.salary = int(input("Ingrese el salario del empleado: "))

        self.imprimir_salario()
        self.paga_impuestos()

    def paga_impuestos(self):
        if self.salary > 3000:
            print(f"El empleado {self.name} paga impuestos")

    def imprimir_salario(self):
        super().imprimir()
        print(f"Salario : {self.salary}")


# --------------------- CODIGO ---------------------#

empleado1 = Empleado()
