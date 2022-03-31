print("Ingrese un año para saber si el año es bisiesto")


def Leap_year(year: int) -> None:
    div4: int = year % 4
    div100: int = year % 100
    div400: int = year % 400
    if div4 & div100 & div400 == 0:
        print("El año es bisiesto")
    elif div4 & div400 == 0:
        print("El año es bisiesto")
    else:
        print("El año no es bisiesto")


year = int(input(""))
Leap_year(year)
