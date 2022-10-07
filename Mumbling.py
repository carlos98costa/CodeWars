def accum(s):
    list = []
    for count, i in enumerate(s):
        list.append(i.upper() + i.lower() * (count))
    return '-'.join(list)
