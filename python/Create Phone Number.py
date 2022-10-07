def create_phone_num(a):
    numb = ""
    count = 0
    for i in a:
        a = "".join([str(i)])
        count = count + 1
        if count == 1:
            numb = numb + "("
        if count == 4:
            numb = numb + ") "
        if count == 7:
            numb = numb + "-"
        numb = numb + str(i)
    return numb