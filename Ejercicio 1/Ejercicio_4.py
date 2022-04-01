def sort_list() -> list:
    list: int = []
    n: int = int(input("Ingrese la cantidad de numeros que tendra su lista : "))

    for i in range(0, n):
        num: int = int(input())

        list.append(num)

    list.sort(reverse=True)
    return list


print(sort_list())
