while True:
    try:
        x = int(input("Ingrese un numero: "))
        y = int(input("Ingrese otro numero: "))

        print("La division es: ", x / y)
        break
    except ValueError:
        print(
            "Error, no ingreso un numero, porfavor ingrese dos numero para poder realizar su division"
        )
    except ZeroDivisionError:
        print(
            "Error, no se puede dividir por cero, porfavor ingrese dos numero diferentes de cero para poder realizar su division"
        )
    finally:
        print("Se termino el programa, gracias por su colaboracion")
