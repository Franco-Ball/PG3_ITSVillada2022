print("Ingrese una frase para contar la cantidad de vocales que hay en ella")
frase: str = input()


def contar_vocales(frase) -> int:
    contador: int = 0
    for ltr in frase:
        if ltr.lower() in "aeiou":
            contador += 1
    return contador


vocales: int = contar_vocales(frase)
print(f"En la cadena '{frase}' hay {vocales} vocales")
