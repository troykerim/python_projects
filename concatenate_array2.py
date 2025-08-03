'''
You are given an integer array nums of length n. 
Create an array ans of length 2n where ans[i] == nums[i] and ans[i + n] == nums[i] for 0 <= i < n (0-indexed).
Specifically, ans is the concatenation of two nums arrays.
Return the array ans.
'''
def getConcatenation(nums: list[int]) -> list[int]:
    n = len(nums)
    ans = [0] * (2 * n)
    for i, num in enumerate(nums):
        ans[i] = ans[i + n] = num
    return ans

nums = [1,4,1,2]
print(getConcatenation(nums))