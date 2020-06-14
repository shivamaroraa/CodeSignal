def shapeArea(n):
    if n == 1:
        return 1
    else:
        m = n - 1
        return m * m + n * n
