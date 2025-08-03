'''
Pair Sum - Sorted
Given an array of integers sorted in ascending order and a target value, 
return the indexes of any pair of numbers in the array that sum to the target. 
The order of the indexes in the result doesn't matter. If no pair is found, return an empty array.

Input: nums = [-5, -2, 3, 4, 6], target = 7
Output: [2, 3]

'''
"""
    Two Pointer approach, opposite Pointers version
"""

def pairsum(nums, target):
    left, right = 0, len(nums) - 1 # Left is at index 0, Right is at last index of nums
    
    while left < right:
        sum = nums[left] + nums[right]
        if sum < target:
            left += 1 
        elif sum > target:
            right -= 1 
        else:
            return [left, right]
    return []
nums = [-5, -2, 3, 4, 6]
target = 10

print(pairsum(nums, target))