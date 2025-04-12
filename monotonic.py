def monotonic(nums):
    if all(nums[i] < nums[i+1] for i in range(len(nums) - 1)):
        return "Increasing"
    elif all(nums[i+1] < nums[i] for i in range(len(nums) - 1)):
        return "Decreasing"
    else:
        return "Not a monotonic sequence!"
    
user_input = input("Enter a list of numbers seperated by spaces: ")
n = list(map(int, user_input.split()))
print(monotonic(n))