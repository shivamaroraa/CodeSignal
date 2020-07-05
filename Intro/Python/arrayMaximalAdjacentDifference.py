def arrayMaximalAdjacentDifference(inputArray):
    diff, i = 0, 0
    while i < len(inputArray) -1:
        if abs(inputArray[i] - inputArray[i +1]) > diff:
            diff = abs(inputArray[i] - inputArray[i +1])
        i +=1
    return diff