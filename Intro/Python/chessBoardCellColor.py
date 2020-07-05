def chessBoardCellColor(cell1, cell2):
    return getColor(cell1) == getColor(cell2)


def getColor(cell):
    if cell[0] == 'A' or cell[0] == 'C' or cell[0] == 'E' or cell[0] == 'G':
        x = 0
    else:
        x = 1

    if (x + int(cell[1])) % 2 != 0:
        return 'Black'
    else:
        return 'White'
