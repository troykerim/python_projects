'''
Find two numbers in an array that add up to a specific target value

** This version allows the user to enter their own array and target, returns true if the target is found

Example: 
Arr = [0 -1 -9 4 2 44 32 -3]
Target = - 4
Returns: True 
'''
def two_sum(arr, target):
    arr.sort()
    left = 0 
    right = len(arr) - 1 
    
    while left < right:
        sum = arr[left] + arr[right]
        if sum == target:
            return True 
        elif sum < target:
            left += 1 
        else:
            right -= 1 
            
    return False 

user_input = input("Enter an array of elements seperated by spaces: ")
arr = list(map(int, user_input.strip().split()))
target = int(input("Enter a target value: "))

if two_sum(arr,target):
    print("true")
else:
    print("false")