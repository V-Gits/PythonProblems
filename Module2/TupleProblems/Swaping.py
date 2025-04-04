"""
Write a python program to input any 2 tuples
and swap them
Sample input :
tuple1 = (1,2,3,4,5)
tuple2 = (10,20,30)
Sample output :
tuple1 = (10,20,30)
tuple2 = (1,2,3,4,5)
"""


tuple1 = tuple(input("Enter the elements of the first tuple, separated by spaces: ").split())
tuple2 = tuple(input("Enter the elements of the second tuple, separated by spaces: ").split())

print("\nOriginal tuples:")
print("Tuple 1:", tuple1)
print("Tuple 2:", tuple2)

tuple1, tuple2 = tuple2, tuple1

print("\nAfter swapping:")
print("Tuple 1:", tuple1)
print("Tuple 2:", tuple2)