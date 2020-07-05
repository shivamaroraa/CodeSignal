def sortByHeight(a):
    temp = []
    length = len(a) - 1
    i = 0
    dict = {}

    while i <= length:
        if a[i] < 0:
            dict[i] = a[i]
        else:
            temp.append(a[i])
        i += 1

    temp.sort()

    result = []

    for k in range(len(a)):
        if k in dict:
            result.append(dict[k])
        else:
            result.append(temp.pop(0))

    return result
