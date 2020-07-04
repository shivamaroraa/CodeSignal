import string


def variableName(name):
    correct_format = list(string.ascii_letters)
    correct_format.extend(string.digits)
    correct_format.append('_')
    print(correct_format)
    if name[0] in string.digits:
        return False
    for i in range(len(name)):
        if name[i] not in correct_format:
            print(name[i])
            return False
    return True



