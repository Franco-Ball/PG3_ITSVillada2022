try:

    f = open("Ejercicios_Manejo_Exceptions/Texto_Ejercicio_5.txt", "w")
    f.write("Bienvenidos al documento de text del Ejercicio 5! \n")
    contenido = input("Ingrese el contenido que quiere agregale al documento: ")

    chars = set("0123456789")

    if all((c in chars) for c in contenido):
        f.write(int(contenido))
    else:
        f.write(contenido)

    f.close()

    print("Ahora veamos como se ve el documento:")

    f = open("Ejercicios_Manejo_Exceptions/Texto_Ejercicio_5.txt", "r")
    print(f.read())
    f.close()
except TypeError:
    print("No se puede ingresar enteros en el metodo write!")
