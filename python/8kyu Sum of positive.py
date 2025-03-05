def positive_sum(arr):
    # Your code here
    sum = 0
    for num in arr:
        if num > 0:
            sum += num
    return sum
