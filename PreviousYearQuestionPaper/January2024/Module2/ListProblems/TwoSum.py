"""
Given a list L and integer target, you have to find a pair of integers whose sum is
equal to given integer target

Sample input: L = [1,2,3,4,5] target = 9
Sample output: (4,5)
"""

def TwoSum(List, target):
    HashMap = dict()
    for i in range(len(List)):
        HashMap[List[i]] = i
    for i in range(len(List)):
        comp = target-List[i]
        if comp in HashMap and comp != HashMap[comp] != i:
            return (List[i], List[HashMap[comp]])


L = [1,2,3,4,5]
target = 9
print(TwoSum(L, target))


#Output
"""
(4, 5)
"""