import string


def isBeautifulString(inputString):
    letters = string.ascii_lowercase
    letters_dictionary = {letter:0 for letter in letters}

    for element in inputString:
        if element in letters_dictionary:
            letters_dictionary[element] +=1
        else:
            return -1

    arr_values = [letters_dictionary[key] for key in letters_dictionary]

    for i in range(len(arr_values)-1):
        if arr_values[i] < arr_values[i+1]:
            print(i)
            return False

    return True