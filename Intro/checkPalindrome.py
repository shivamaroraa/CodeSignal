def checkPalindrome(inputString):
    isP = True
    for i in range(len(inputString)):
        if inputString[i] != inputString[len(inputString) - 1 - i]:
            isP = False

    return isP