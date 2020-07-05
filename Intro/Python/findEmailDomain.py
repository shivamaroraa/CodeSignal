def findEmailDomain(address):
    a = re.split('@', address)
    return a[len(a)-1]
