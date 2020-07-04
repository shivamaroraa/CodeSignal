def messageFromBinaryCode(code):
    message = ''
    char_arr = [code[i:i+8] for i in range(0, len(code), 8)]
    print(char_arr)
    for bits in char_arr:
        bits = chr(int(bits,2))
        message+= bits
    
    return message           
