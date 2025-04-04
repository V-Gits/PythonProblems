"""
arr = np.array([3, 10, 7, 15, 21, 30, 45])
Find all the elements that are divisible by both 3 and 5.
"""
import numpy as np

arr = np.array([3, 10, 7, 15, 21, 30, 45])
mask = (arr % 3 == 0) & (arr % 5 == 0)
result = arr[mask]

print(f"Numbers divisible by both 3 anf 5: ", result)