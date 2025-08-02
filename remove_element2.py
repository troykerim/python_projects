"""
    Remove an element from a list
    
    User decides how big the list is and what values to put into the list
    User then decides what value they want to be removed from the list
"""
# Create an empty list
nums = []

x = int(input("How big do you want your list: "))
for i in range(x):
    y = int(input(f"Enter element number {i+1}: "))
    nums.append(y)

print("Here is the original list: ", nums)
    
remove = int(input("Enter a number you want to be removed: "))

# Remove elements using remove() in a loop
while remove in nums:
    nums.remove(remove)
        
print("Here is the new version of the list: ", nums)