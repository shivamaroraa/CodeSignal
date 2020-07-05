def isDigit(symbol):
    try:
        int(symbol)
        return True
    except:
        return False
