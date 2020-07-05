import itertools


def stringsRearrangement(inputArray):
    strcount = len(inputArray)
    perms = [x for x in itertools.permutations(inputArray)]
    for i in range(0, len(perms)):  
        broken = 0 
        for j in range(1, strcount): 
            first = [a for a in perms[i][j]]
            second = [b for b in perms[i][j-1]]
            if sum([first[k] != second[k] for k in range(0,len(first))]) != 1:
                broken = broken + 1
        if broken == 0:
            return True    
    return(False)