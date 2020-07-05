from itertools import groupby


def lineEncoding(s):
    result = ""
    arr = ["".join(grp) for num, grp in groupby(s)]
    for char in arr:
        if len(char) > 1:
            result += str(len(char)) + char[0]
        else:
            result += char[0]
    return result

