def evenDigitsOnly(n):

    n = str(n)
    for i in range(len(n)):
        if int(n[i]) % 2 != 0:
            return False
    return True

