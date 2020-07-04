def deleteDigit(n):
    n = str(n)
    nums = [int(x) for x in n]
    print(nums)
    arr = []

    temp = nums.copy()

    for i in range(len(temp)):
        temp.pop(i)
        t = ''.join(str(x) for x in temp)
        arr.append(int(t))
        temp = nums.copy()


    return max(arr)
