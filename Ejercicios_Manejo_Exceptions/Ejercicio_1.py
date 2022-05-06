while True:
    try:
        x = int(input("Ingrese un numero: "))
        y = int(input("Ingrese otro numero: "))

        print("La suma es: ", x + y)

        while True:
            flag = input("¿Desea seguir sumando valores? (S/N) ")
            if flag == "S":
                continue
            elif flag == "N":
                exit()
            else:
                print("Ingrese una opcion valida!")

    except ValueError:
        print(
            "Error, no ingreso un numero, porfavor ingrese dos numero para poder realizar su suma"
        )
