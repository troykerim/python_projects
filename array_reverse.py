import array

a = array.array('i', [1, 2, 3, 4, 5])

print("Here is the original array: ")
for i in a:
    print(i, end=' ')

# Pointers
left = 0
right = len(a) - 1

while left < right:
    # Swap elements at left and right
    temp = a[left]
    a[left] = a[right]
    a[right] = temp

    # Move pointers 
    left += 1
    right -= 1

print("\nHere is the array reversed: ")
for i in a:
    print(i, end=' ')
print()

