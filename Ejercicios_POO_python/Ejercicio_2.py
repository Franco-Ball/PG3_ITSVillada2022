# ---------------------- CLASE ALUMNO ----------------------#
class Alumno:
    def inicializar(self, name, nota):
        self.name = name
        self.nota = nota

    def imprimir(self):
        if self.nota >= 6 and self.nota <= 10:
            print(f"El alumno {self.name} esta aprobado con una nota de {self.nota}")
        elif self.nota >= 0 and self.nota < 6:
            print(f"El alumno {self.name} esta desaprobado con una nota de {self.nota}")
        else:
            print(f"La nota del alumno {self.name} es invalida")


# ---------------------- CODIGO ----------------------#

Alumno1 = Alumno()
Alumno1.inicializar(
    input("Ingrese el nombre del alumno 1: "),
    int(input("Ingrese la calificacion del alumno: ")),
)

Alumno2 = Alumno()
Alumno2.inicializar(
    input("Ingrese el nombre del alumno 2: "),
    int(input("Ingrese la calificacion del alumno: ")),
)

Alumno1.imprimir()
Alumno2.imprimir()
