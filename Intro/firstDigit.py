import numbers

def firstDigit(inputString):
    
    digits = ['0','1','2','3','4','5','6','7','8','9']
    for i in range(len(inputString)):
        if inputString[i] in digits:
            return inputString[i]

