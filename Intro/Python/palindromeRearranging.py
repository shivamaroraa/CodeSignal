def palindromeRearranging(s):
    c = [s.count(i)%2 for i in set(s)]
    return sum(c)<=1