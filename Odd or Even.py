def odd_or_even(arr):
    soma = sum(arr)
    res = ""
    if soma % 2 == 0:
        res= "even"
    else:
        res = "odd"
    return res
