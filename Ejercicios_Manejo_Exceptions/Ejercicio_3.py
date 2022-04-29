meses = (
    "Enero",
    "Febrero",
    "Marzo",
    "Abril",
    "Mayo",
    "Junio",
    "Julio",
    "Agosto",
    "Septiembre",
    "Octubre",
    "Noviembre",
    "Diciembre",
)

while True:
    try:
        mes = int(input("Ingrese un numero: "))
        print("El mes es: ", meses[mes - 1])
        break
    except IndexError:
        print(
            "Error, no ingreso un numero valido, porfavor ingrese un numero entre 1 y 12"
        )
    except ValueError:
        print("Error, no ingreso un numero, porfavor ingrese un numero entre 1 y 12")
