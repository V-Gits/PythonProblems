"""
Generate a 4x4 NumPy array with random integers between 1 and 100.
Find the row-wise and column-wise sum of the array.
"""

import numpy as np
matrix = np.random.randint(1, 101,(4,4))
row_sum = np.sum(matrix, axis=1)
col_sum = np.sum(matrix, axis=0)    
print(f"""
Random 4x4 Matrix: \n{matrix}
Row Wise Sum: {row_sum}
Column Wise Sum: {col_sum}
        """)