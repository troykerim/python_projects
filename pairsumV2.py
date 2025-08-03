'''
Pair Sum - Sorted
Given an array of integers sorted in ascending order and a target value, 
return the indexes of any pair of numbers in the array that sum to the target. 
The order of the indexes in the result doesn't matter. If no pair is found, return an empty array.

Input: nums = [-5, -2, 3, 4, 6], target = 7
Output: [2, 3]
'''

"""
    Brute force approach
    This solution involves checking all possible pairs. 
    This is done using two nested loops: an outer loop that traverses the array for the first element of the pair, 
    and an inner loop that traverses the rest of the array to find the second element.
"""
def pairsum(nums, target):
    n = len(nums)
    for i in range(n):
        for j in range(i + 1, n):  # i + 1 b/c we want to look at the next index (0,1) for example is the start
            if nums[i] + nums[j] == target: 
                return [i, j] # If a pair was found, return both indexes
    
    return [] # If no pair was found, return an empty array

nums = [-5, -2, 3, 4, 6]
target = 7

print(pairsum(nums, target))