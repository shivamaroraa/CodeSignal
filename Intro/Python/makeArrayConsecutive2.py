def makeArrayConsecutive2(statues):
    statues.sort()
    a = statues[len(statues) - 1] - statues[0] + 1
    return a - len(statues)
