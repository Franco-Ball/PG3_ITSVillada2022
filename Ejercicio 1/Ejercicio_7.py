print("Ingrese un numero para verificar si es step")

num = input()


def isStep(num):
    num = str(num)
    prevDigit = int(num[0]) - 1

    for i in str(num):
        if int(i) - 1 == prevDigit or int(i) + 1 == prevDigit:
            prevDigit = int(i)
            continue
        else:
            return False

    return True


step = isStep(num)
print(step)
