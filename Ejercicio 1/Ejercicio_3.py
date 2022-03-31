print("Ingrese el ancho del rectangulo")
ancho = int(input(""))
print("Ingrese el alto del rectangulo")
alto = int(input(""))
print("Ingrese el caracter con el que se representara el rectangulo")
carac = str(input(""))


def Rectangle(ancho: int, alto: int, carac: str) -> None:
    for x in range(alto):
        print(ancho * carac)


print("----------")
Rectangle(ancho, alto, carac)
print("----------")
