List: int = [14, 8, 3, 6, 2, 9, 1, 4, 15, 11, 7, 10, 5, 12, 13]


def Get_list_index(List: list, number: int) -> None:
    for x in List:
        if x == number:
            index: int = List.index(number)
            print(f"El numero que buscaste esta en el indice: " + {index})


print("La lista contiene numeros del 1 al 15!")
print("Ingrese el numero que quiere buscar en la lista para obtener su indice")
num: int = int(input(""))

Get_list_index(List, num)
