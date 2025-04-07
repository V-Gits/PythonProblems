def summation(lower, upper):
    """
    This Function returns the sum of the number in between the given range of two numbers
    """
    sum = 0
    for i in range(lower, upper):
        sum+=i
    return sum

print(summation(5, 20))
print(help(summation))