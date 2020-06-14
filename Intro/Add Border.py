def addBorder(picture):
    pic_len = len(picture)
    word_len = len(picture[0])

    presuff = "**"
    for i in range(word_len):
        presuff += "*"

    result = [presuff]

    for i in range(pic_len):
        element = picture[i]
        result_element = '*' + element + '*'
        result.append(result_element)

    result.append(presuff)

    return result
