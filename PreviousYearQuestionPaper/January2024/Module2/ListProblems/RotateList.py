"""
Given a List L, rotate the list k times in the clockwise direction

Sample input : L = [1,2,3,4,5] k = 2
Sample output : [4,5,1,2,3]
"""

def rotate(List, k):
    newList = [0]*5
    for i in range(len(List)):
        newList[(i+k)%len(List)] = List[i]
    return newList

L = [1,2,3,4,5]
k = 2
print(rotate(L, k))

#Output
"""
[4, 5, 1, 2, 3]
"""