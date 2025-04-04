"""
arr = np.array([[10, 20, 30, 40],  
                [50, 60, 70, 80],  
                [90, 100, 110, 120]])
Extract a subarray containing only the second and third columns.
"""

import numpy as np 


arr = np.array([[10, 20, 30, 40],  
                [50, 60, 70, 80],  
                [90, 100, 110, 120]])

print(arr[:, 1:3])