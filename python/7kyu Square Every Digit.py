def square_digits(num):
    # Your code here
    bla = ""
    new = str(num)
    for i in new:
        i = int(i) ** 2
        i = str(i)
        bla = bla + i
    return int(bla)
