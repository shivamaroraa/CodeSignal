def adjacentElementsProduct(inputArray):

    products = []
    for i in range(len(inputArray) - 1):
        products.append(inputArray[i] * inputArray[i + 1])

    return max(products)