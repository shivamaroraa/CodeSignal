def circleOfNumbers(n, firstNumber):
    arr = []
    for i in range(n):
        arr.append(i)

    return arr.index(((int(n / 2) + arr.index(firstNumber))) % n)
