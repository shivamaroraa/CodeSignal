def boxBlur(image):
    new_image = [ [] for i in range(len(image) - 3 + 1)]
    for i in range(len(image[0]) - 3 + 1):
        for j in range(len(image) - 3 + 1):
            new_image[j].append( (sum(image[j][i:i+3]) + sum(image[j+1][i:i+3]) + sum(image[j+2][i:i+3])) //9)

    return new_image
