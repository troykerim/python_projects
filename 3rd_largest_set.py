def largest(nums):
    nums = set(nums)
    if len(nums) < 3:
        return None 
    
    nums = list(nums)
    nums.sort(reverse=True)
    
    return nums[2]
nums = [1,2,3,4,5,6,7,8,9]
print("Original List of numbers: ")
print(nums)

print("3rd largest number of the same list: ")
print(largest(nums))