def print_rectangle() -> None:
    ancho: int = int(input("Ingrese el ancho del rectangulo: "))
    alto: int = int(input("Ingrese el alto del rectangulo: "))
    carac: str = str(
        input("Ingrese el caracter con el que se representara el rectangulo: ")
    )

    for x in range(alto):
        print(ancho * carac)


print_rectangle()
