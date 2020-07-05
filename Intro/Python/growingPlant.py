def growingPlant(upSpeed, downSpeed, desiredHeight):
    number_days = 0
    height = 0
    while height < desiredHeight:
        height += upSpeed
        number_days +=1
        if height >= desiredHeight:
            break
        height -= downSpeed
        
    
    return number_days
