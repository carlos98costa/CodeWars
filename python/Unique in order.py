def unique_in_order(iterable):
    list = []
    letter = ""
    for i in iterable:
        if i != letter:
            letter = i
            list.append(i)
    return list

