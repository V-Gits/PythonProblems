"""
Given a list nums of numbers and an integer val, remove all occurences of val in the
list
Sample input : nums = [1,2,2,3,4,5,6,6,2,2,2,8] val = 2
Sample output : [ 1,3,4,5,6,6,8]
"""

def removeOccurannce(List, k):
    return [i for i in List if i != k]

nums = [1,2,2,3,4,5,6,6,2,2,2,8]
val = 2
print(removeOccurannce(nums, val))

#Output
"""
[1, 3, 4, 5, 6, 6, 8]
"""