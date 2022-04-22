# ---------------------- CLASE TRIANGULO ----------------------#
class Trinagulo:
    def inicializar(self, lado1, lado2, lado3):
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3

    def imprimir(self):
        if self.lado1 == self.lado2 and self.lado2 == self.lado3:
            print("El triangulo es equilatero")
        elif self.lado1 > self.lado2 and self.lado2 > self.lado3:
            print(f"El lado uno es el lado mas grande con un valor de : {self.lado1}")
        elif self.lado1 < self.lado2 and self.lado2 > self.lado3:
            print(f"El lado dos es el lado mas grande con un valor de : {self.lado2}")
        else:
            print(f"El lado tres es el lado mas grande con un valor de : {self.lado3}")


# ---------------------- CODIGO ----------------------#

triangulo = Trinagulo()
triangulo.inicializar(
    int(input("Ingrese el valor del lado 1: ")),
    int(input("Ingrese el valor del lado 2: ")),
    int(input("Ingrese el valor del lado 3: ")),
)

triangulo.imprimir()
