"""
Create a function min_max() that takes n numbers as list argument and return the
smallest and largest numbers.
"""

def min_max(numbers):
    Min = numbers[0]
    Max = numbers[0]
    for i in numbers:
        if i < Min:
            Min = i
        if i > Max:
            Max = i
    return(Min, Max)

L = [1,2,3,4,5,6,7,8,9]
print(min_max(L))