def spiralNumbers(n):
    result = [[0] * n for _ in range(n)]
    
    x_direction = (0, 1, 0, -1)
    y_direction = (1, 0, -1, 0)
    
    x, y, counter = 0, -1, 1
    
    for i in range(n + n - 1):
        for j in range((n + n - i)//2):
            x += x_direction[i % 4]
            y += y_direction[i % 4]
            result[x][y] = counter
            counter += 1
            
    return result