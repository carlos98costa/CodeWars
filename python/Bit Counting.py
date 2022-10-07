def count_bits(n):
    bindata = format(n, "b")
    count = 0
    for i in bindata:
        if i == "1":
            count = count + 1
    return count