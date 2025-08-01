'''
    "Remove the duplicate values from a sorted list" Version 1
    1. Create a list and fill in elements into the list
    2. Modify the list so that all elements are sorted
    3. Modify the sorted list so that any duplicate elements are removed
'''
def remove(my_list):
    return list(sorted(set(my_list))) # set() will automatically eliminate duplicate items.
    # sorted() and list() are technically redundant but ensures that the list remains is a list and is sorted
    
# 1. Create an empty list
my_list = []

# Enter elements into the list. Lists are dynamic 
num_elements = int(input("Enter the number of elements: "))
for i in range(num_elements):
    element = input(f"Enter element {i+1}: ")
    my_list.append(element)

print("The original list:", my_list)

# 2. Sort the elements in the list
my_list.sort() 
print("\nThe list sorted:", my_list)
# Use the method .sort() and not the function sorted(var_name)!

# 3. Remove duplicates
print("Here is the list with duplicates removed: ", remove(my_list))