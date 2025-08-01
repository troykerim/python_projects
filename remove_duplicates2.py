'''
    "Remove the duplicate values from a sorted list" Version 2
    1. Create a list and fill in elements into the list
    2. Modify the list so that all elements are sorted
    3. Modify the sorted list so that any duplicate elements are removed
'''


def remove_dup_sorted(input_list):
    # Bound checking, if the list is empty, return an empty list
    if not input_list:
        return []

    # Create a new list to contain non duplicate values
    # Copy the first element
    result = [input_list[0]] 

    '''
    Interate over the entire list. Start at index 1 (not 0)
    '''
    for i in range(1, len(input_list)):
        # Compare ith element with previous element
        # If they are not equal, add that element to the result list
        if input_list[i] != input_list[i - 1]: 
            result.append(input_list[i])

    return result

my_list = [1, 1, 2, 3, 3, 4, 5, 5, 8]
print("Here is the original list: ", my_list)
unique_list = remove_dup_sorted(my_list)
print("Here is the list with duplicates removed: ", unique_list)

my_list2 = [2,10,10,30,30,30]
print("Here is the original list: ", my_list2)
unique_list2 = remove_dup_sorted(my_list2)
print("Here is the list with duplicates removed: ", unique_list2)

my_list3 = []
print("Here is the original list: ", my_list3)
unique_list3 = remove_dup_sorted(my_list3)
print("Here is the list with duplicates removed: ", unique_list3)