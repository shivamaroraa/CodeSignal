def avoidObstacles(inputArray):
    max = 0
    for element in inputArray:
        if max < element:
            max = element

    best_hop = max + 1

    possible_hops = []
    for i in range(1, max + 2):
        if i not in inputArray:
            possible_hops.append(i)
            for element in inputArray:
                if element % i == 0 and i in possible_hops:
                    possible_hops.pop(possible_hops.index(i))

    return possible_hops[0]