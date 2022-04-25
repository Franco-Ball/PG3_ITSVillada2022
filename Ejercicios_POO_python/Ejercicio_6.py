# --------------------- CLASE FAMILIA ---------------------#
class Familia:
    def __init__(self) -> None:
        self.name_padre = input("Ingrese el nombre del padre: ")
        self.name_madre = input("Ingrese el nombre de la madre: ")
        self.names_hijos = input(
            "Ingrese los nombres de los hijos separados por un espacio: "
        ).split()

    def __str__(self) -> str:
        return f"Padre: {self.name_padre}\nMadre: {self.name_madre}\nHijos: {self.names_hijos}"


# --------------------- CODIGO ---------------------#

familia1 = Familia()
print(familia1)
