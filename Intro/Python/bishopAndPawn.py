def bishopAndPawn(bishop, pawn):
    row = abs(ord(bishop[0]) - ord(pawn[0]))
    col = abs(int(bishop[1]) - int(pawn[1]))
    
    return row == col