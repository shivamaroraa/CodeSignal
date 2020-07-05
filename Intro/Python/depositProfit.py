def depositProfit(deposit, rate, threshold):
    year = 0
    while deposit < threshold:
        deposit *= (rate+ 100)/100
        year +=1
    
    return year
        

