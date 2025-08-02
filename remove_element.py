'''
Remove Element - Version 1 
You are given an integer array nums and an integer val. Your task is to remove all occurrences of val from nums in-place.

After removing all occurrences of val, return the number of remaining elements, say k, such that the first k elements of nums do not contain val.

Note:

The order of the elements which are not equal to val does not matter.
It is not necessary to consider elements beyond the first k positions of the array.
To be accepted, the first k elements of nums must contain only elements not equal to val.

Return k as the final result.

Input: nums = [1,1,2,3,4], val = 1

Output: [2,3,4].  Returning k = 3, we have 3 values NOT equal val = 1.
You return the # of elements that were found to be NOT equal val

'''

"""
    Used Two Pointer (Read/Write Version)
    Read Pointer: "read/fast pointer" iterates through the entire data structure, reading elements.
    
    Write Pointer: "write/slow pointer" is responsible for placing elements into their correct, modified positions within the same data structure. 
    This pointer only moves when a valid element is found and needs to be written.
"""
def remove_element(nums, val):   
    k = 0 # Write Pointer
    for i in range(len(nums)): # i = read pointer
        if nums[i] != val:
            nums[k] = nums[i] # Not necessary
            k += 1

    return k

nums = [1, 1, 2, 3, 4]
val = 1

# nums = [1, 2, 2, 2, 6, 9, 10, 22]
# val = 2

print("Original list: ", nums)
print("Target value: ", val)
print("Number of elements not equal to target value of: ", remove_element(nums, val))