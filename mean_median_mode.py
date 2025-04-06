# Mean, Median, Mode
def mean(val):
    average = sum(val) / len(val)
    return average
    
def median(val):
    sorted_list = sorted(val) # Sort the list before caluclating median
    n = len(sorted_list) # need the number of elements in list
    
    if n % 2 == 1:  # If their is an odd number of elements
        return sorted_list[n // 2]
    else:
        mid1, mid2 = sorted_list[n // 2 - 1], sorted_list[n // 2]
        return (mid1 + mid2) / 2 
        

def mode(val):
    freq = {}
    max_freq = 0
    modes = []
    
    for num in val:
        freq[num] = freq.get(num, 0) + 1 
        if freq[num] > max_freq:
            max_freq = freq[num]
            modes = [num]
        elif freq[num] == max_freq:
            modes.append(num)
    return modes
            


val = []

n = int(input("Input a range for the list: "))

for i in range(n):
    nums = int(input(f"Enter element {i+1}: "))
    val.append(nums)
    
print("Your list:", val)
# print(sorted(val))
print("The mean is:", mean(val))
print("The median is:", median(val))
print("The mode is:", mode(val))