import re


def isMAC48Address(inputString):
    
    valid_letters = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F"]
    l = re.split('-', inputString)

    for part in l:
        if len(part) != 2:
            return False
        for digit in part:
            print(digit)
            if digit not in valid_letters:
                return False
    return True