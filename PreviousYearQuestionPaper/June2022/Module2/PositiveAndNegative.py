"""
Write a Python program to read n integers into a list and separate the positive
and negative numbers into two different lists.
"""

L = [1,-2,2,-4,3,-6]
pos = [x for x in L if x >= 0]
neg = [x for x in L if x < 0]
print(pos)
print(neg)