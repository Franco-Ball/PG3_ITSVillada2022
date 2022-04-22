# ---------------------- CLASE OPERACIONES ----------------------#
class Operaciones:
    def __init__(self) -> None:
        self.num1 = input("Ingrese el primer numero: ")
        self.num2 = input("Ingrese el segundo numero: ")
        print(
            f"El resultado de la suma entre {self.num1} y {self.num2} es : {self.suma()}"
        )
        print(
            f"El resultado de la resta entre {self.num1} y {self.num2} es : {self.resta()}"
        )
        print(
            f"El resultado de la multiplicacion entre {self.num1} y {self.num2} es : {self.multiplicacion()}"
        )
        print(
            f"El resultado de la division entre {self.num1} y {self.num2} es : {self.division()}"
        )

    def suma(self):
        return int(self.num1) + int(self.num2)

    def resta(self):
        return int(self.num1) - int(self.num2)

    def multiplicacion(self):
        return int(self.num1) * int(self.num2)

    def division(self):
        return int(self.num1) / int(self.num2)


# ---------------------- CODIGO ----------------------#
Operacion1 = Operaciones()
