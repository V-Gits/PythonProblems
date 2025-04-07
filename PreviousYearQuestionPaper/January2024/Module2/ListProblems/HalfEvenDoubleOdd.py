"""
Write a Python program that inputs a list of numbers and then doubles the odd
numbers and halves the even numbers
"""

def halfEvendoubleOdd(List):
    return [x*2 if x%2 != 0 else x/2 for x in List]

L = [1,2,3,4,5]
print(halfEvendoubleOdd(L))

#Output

"""
[2, 1.0, 6, 2.0, 10]
"""