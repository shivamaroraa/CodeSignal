def digitsProduct(product):
    if product == 0:
        return 10
    if product < 10:
        return product

    for n in range(9, 1, -1):
        if (product % n == 0):
            if digitsProduct(product / n) == -1:
                return -1
            else:
                return int(str(int(digitsProduct(product / n))) + str(n))
    
    return -1