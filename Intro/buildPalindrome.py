def buildPalindrome(st):
    index = 0
    rev = st[::-1]

    while not check_palindrome(rev):
        rev = st[::-1]
        rev = st[0:index] + rev
        index += 1

    return rev


def check_palindrome(string):
    if string == string[::-1]:
        return True
    return False
