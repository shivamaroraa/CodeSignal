def differentSymbolsNaive(s):
    dictionary = {}
    for i in range(len(s)):
        if s[i] not in dictionary:
            dictionary[s[i]] = 1
        else:
            dictionary[s[i]] += 1
    return len(dictionary)
