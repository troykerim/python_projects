'''
Two Sums problem (Basic Version)

Given an array of integers and an integer target,
return 2 indices i and j such that nums[i] + nums[j] == target and where i != j.

Example: target = 10
nums = [3, 5, 8, 5, 1]
Returns: [1,3]

'''
def two_sums(nums, target):
    x = len(nums)
    for i in range(x):
        for j in range(i+1, x):
            if nums[i] + nums[j] == target:
                return [i,j]
    return None
    # print(nums)         Debugging

nums = [] 
target = int(input("Enter a target number: "))
x = int(input("Enter a range: "))

# Fill nums list
for i in range(x):
    w = int(input(f"Enter element number {i + 1}: "))
    nums.append(w)

result = two_sums(nums, target)
print(result)
    