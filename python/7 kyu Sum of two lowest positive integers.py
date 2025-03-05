def sum_two_smallest_numbers(numbers):
    numbers.sort()
    return sum(numbers[0:2])

sum_two_smallest_numbers([5, 8, 12, 18, 22])