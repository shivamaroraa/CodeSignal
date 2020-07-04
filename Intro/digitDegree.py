def digitDegree(n):
    if n <= 9:
        return 0
    else:
        temp = str(n)
        count = 0
        while len(str(temp)) != 1:
            sum_temp = 0
            for i in temp:
                sum_temp += int(i)
            count += 1
            temp = str(sum_temp)
        return count