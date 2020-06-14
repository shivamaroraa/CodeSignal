def allLongestStrings(inputArray):
    longest_length = 0
    for i in range(len(inputArray)):
        if len(inputArray[i]) >= longest_length:
            longest_length = len(inputArray[i])
    result = []
    for j in range(len(inputArray)):
        if longest_length == len(inputArray[j]):
            result.append(inputArray[j])

    return result
