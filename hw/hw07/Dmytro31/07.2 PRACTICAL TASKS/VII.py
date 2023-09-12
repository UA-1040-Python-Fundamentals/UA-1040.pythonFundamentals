def sum_of_multiples(number):
    if number < 0:
        return 0

    total_sum = 0
    for i in range(number):
        if i % 3 == 0 or i % 5 == 0:
            total_sum += i
    return total_sum

# Test examples
print(sum_of_multiples(10))
print(sum_of_multiples(20))
print(sum_of_multiples(-5))