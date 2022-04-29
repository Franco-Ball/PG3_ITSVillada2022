while True:
    try:
        x = int(input("Ingrese un numero: "))
        y = int(input("Ingrese otro numero: "))

        print("La suma es: ", x + y)
        break
    except ValueError:
        print(
            "Error, no ingreso un numero, porfavor ingrese dos numero para poder realizar su suma"
        )
