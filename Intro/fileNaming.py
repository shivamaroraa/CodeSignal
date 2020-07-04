def fileNaming(names):
    result = []
    for name in names:
        if name not in result:
            result.append(name)
            
        else:
            new = name
            count =1
            while new in result:
                new = '%s(%i)' % (name, count)
                count+=1
                if new not in result:
                    result.append(new)
                    break
                
    return result
    


