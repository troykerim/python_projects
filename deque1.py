from collections import deque 

# Create a Deque 
nums = deque([1,2,3,4,5])
print(f"Initial deque: {nums}")

# Adding elements to both sides
nums.append(6)      # Appends to right end (Back)
nums.appendleft(0)  # Appends to left end  (Front)

print(f"\nAfter adding elements: {nums}")

# Removing elements
right_elment = nums.pop()       # Removes from the right end 
left_element = nums.popleft()   # Removes from the left end
print(f"\nElement popped from the right: {right_elment}")
print(f"\nElement popped from the left: {left_element}")

print(f"\nFinal deque: {nums}")