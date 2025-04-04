"""
Create a 3x3 NumPy array with values ranging from 1 to 9. Then, replace all even numbers with 0.
"""

import numpy as np 

matrix = np.arange(1,10).reshape(3,3)
print(f"Matrix before Manipulation: \n{matrix}")
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if matrix[i][j]%2 == 0:
            matrix[i][j] = 0
print(f"Matrix After Manipulation: \n{matrix}")