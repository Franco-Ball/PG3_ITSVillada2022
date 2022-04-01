print("Ingrese una palabra para verificar si es un palindromo")
word: str = input()


def esCapicua() -> bool:

    if str(word) == str(word)[::-1]:
        print("True")
    else:
        print("False")


esCapicua()
