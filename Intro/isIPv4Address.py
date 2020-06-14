def isIPv4Address(inputString):
    try:
        IP = [int(i) for i in inputString.split(".")]
        return max(IP) < 256 and len(IP) == 4
    except:
        return False