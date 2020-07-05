def reverseInParentheses(a):
    for i in range(len(a)):
        if a[i] == "(":
            x = i
        if a[i] == ")":
            y = i
            return reverseInParentheses(a[:x] + a[x + 1:y][::-1] + a[y + 1:])
    return a
