'''
Given an integer array of numbers,
return true is any value appears more than once in the array, otherwise return false
'''
def dup (num_list):
    return len(num_list) != set(num_list)

num_list = [] # Create an empty list

x = int(input("Enter a range: "))  # How big the list should be 
for i in range(x):
    a = int(input(f"Enter a element {i+1}: "))
    num_list.append(a)
print("Here is the original number list:", num_list)
print("\nChecking for duplicate values")


result = dup(num_list)
if result == True:
    print("Your list has duplicates!")
else:
    print("Your list does not have any duplicates!")