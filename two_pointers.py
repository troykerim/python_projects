# 2 Pointers 

def hasPair(nums, target):
    left = 0 
    right = len(nums) - 1 
    while(left < right):
        s = nums[left] + nums[right]
        if s == target:
            return True 
        elif s < target:
            left += 1
        else:
            right -= 1 
    return False 

nums = [1, 2, 4, 6, 8, 9, 14, 15]
target = 13 
result = hasPair(nums, target)
print(result)