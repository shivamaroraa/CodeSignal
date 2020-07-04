def chessKnight(cell):
    cell = (ord(cell[0].lower()) - ord('a') + 1, int(cell[1]))
    move = (-2, -1, 1, 2)
    s = 0
    for i in move:
        for j in move:
            if abs(i) + abs(j) == 3:
                if 1 <= cell[0] + i <= 8 and 1 <= cell[1] + j <= 8:
                    s += 1
    return s