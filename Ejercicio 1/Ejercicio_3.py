def print_equilateral_triangle() -> None:
    n = int(input("Ingrese el alto del triangulo: "))
    char = input("Ingrese el caracter con el que se representara el triangulo: ")
    for i in range(n):
        print(" " * (n - i - 1) + (char + " ") * (i + 1))


def print_rectangle() -> None:
    ancho: int = int(input("Ingrese el ancho del rectangulo: "))
    alto: int = int(input("Ingrese el alto del rectangulo: "))
    carac: str = str(input("Ingrese el caracter con el que se representara el rectangulo: "))

    for x in range(alto):
        print(ancho * carac)


print(
    "Este programa le permite crear un triangulo equilatero o un rectangulo, seleccione la opcion deseada: "
)
print("1. Triangulo equilatero")
print("2. Rectangulo")

opt: int = int(input("Ingrese la opcion deseada: "))

if opt == 1:
    print_equilateral_triangle()
elif opt == 2:
    print_rectangle()
else:
    print("Opcion no valida")