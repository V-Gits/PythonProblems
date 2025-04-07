"""
Write a Python program to accept values from user. Add it to a tuple and display the elements one by one. 
Find the maximum and minumun values of the tuple
"""

values = []
n = int(input("Enter the number of elements you want in the tuple: "))
for i in range(n):
    value = int(input(f"Enter element {i + 1}: "))
    values.append(value)
values_tuple = tuple(values)
print("\nThe elements of the tuple are:")
for element in values_tuple:
    print(element)
max_value = max(values_tuple)
min_value = min(values_tuple)
print(f"\nThe maximum value in the tuple is: {max_value}")
print(f"The minimum value in the tuple is: {min_value}")