List = [14,8,3,6,2,9,1,4,15,11,7,10,5,12,13]

def Get_list_index(List, number):
    for x in List:
        if x == number:
            index = List.index(number) 
            print("El numero que buscaste esta en el indice: " + str(index))

print("La lista contiene numeros del 1 al 15!")
print("Ingrese el numero que quiere buscar en la lista para obtener su indice")
num = int(input(""))

Get_list_index(List, num)