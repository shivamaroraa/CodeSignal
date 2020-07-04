import string

def alphabeticShift(inputString):

    alphabets = string.ascii_lowercase
    result = ''

    for i in range(len(inputString)):
        position = (alphabets.rindex(inputString[i]) + 1) % 26
        result += alphabets[position]

    return result

