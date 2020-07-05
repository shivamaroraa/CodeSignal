def longestDigitsPrefix(inputString):
    regex = '^[0-9]+'
    x = re.match(regex, inputString)
    if x is not None:
        return x.group()
    else:
        return ''
    
