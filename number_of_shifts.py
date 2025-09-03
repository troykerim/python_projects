'''
Write a function that counts the number of shifts (element moves) required to sort an array using Insertion Sort.

'''

def count_shifts(arr):
    shifts = 0  # Initialize shift counter
    
    for i in range(1, len(arr)):  # Traverse the array
        key = arr[i]  # Take the current element
        j = i - 1
        
        # Shift elements to make space for key
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
            shifts += 1  # Count each shift
        arr[j + 1] = key  # Place key at the correct position
    return shifts  # Return total shifts count
 
arr = [8, 4, 3, 7, 2, 11, 50, 6, 3]
print("Number of shifts:", count_shifts(arr))