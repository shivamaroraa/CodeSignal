def sumUpNumbers(s):
    return sum(map(int, re.findall(r'\d+', s)))