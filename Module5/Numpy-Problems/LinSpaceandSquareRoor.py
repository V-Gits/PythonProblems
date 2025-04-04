"""
Question 3: Mathematical Operations
Create a NumPy array of 10 linearly spaced values between 5 and 50. 
Then, find the square root of each element in the array.
"""

import numpy as np 

arr = np.linspace(5,50,10)

sqrt_arr = np.sqrt(arr)

print(f"Orginal Array: {arr}\n Square Root Array: {sqrt_arr}")