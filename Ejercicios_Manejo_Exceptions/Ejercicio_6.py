import mysql.connector

miConexion = mysql.connector.connect(
    host="localhost", user="franco", passwd="pepe1234", db="Ej_Excepciones"
)

cur = miConexion.cursor()

while True:

    try:
        command = input("Ingrese un comando: ")
        cur.execute(command)

    except mysql.connector.errors.ProgrammingError as e:
        print("Error")
        print(e)
        print(type(e))

    except mysql.connector.errors.OperationalError as e:
        print("Error")
        print(e)
        print(type(e))

    except mysql.connector.errors.DataError as e:
        print("Error")
        print(e)
        print(type(e))

    except mysql.connector.errors.InterfaceError as e:
        print("Error")
        print(e)
        print(type(e))

    except mysql.connector.errors.DatabaseError as e:
        print("Error")
        print(e)
        print(type(e))

    flag = input("¿Desea continuar? (S/N)")
    if flag == "N":
        break


miConexion.close()
