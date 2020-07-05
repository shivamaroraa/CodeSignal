def isLucky(n):
    n = str(n)
    half = len(n) // 2
    n1, n2 = n[: half], n[half:]

    sum1, sum2 = 0, 0
    for i in range(half):
        sum1 += int(n1[i])
        sum2 += int(n2[i])

    return sum1 == sum2
