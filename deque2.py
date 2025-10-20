from collections import deque
def list_append_left(n):
  """Add elements to the beginning of a list."""
  lst = []
  for i in range(n):
    lst.insert(0, i)  # Insert at the beginning (expensive for lists)
  return lst

def deque_append_left(n):
  """Add elements to the beginning of a deque."""
  d = deque()
  for i in range(n):
    d.appendleft(i)   # Append to the left (efficient for deques)
  return d

# Demonstrate bidirectional functionality
d = deque([1, 2, 3])
print("\nBidirectional operations demonstration:")
print(f"Initial deque: {d}")

# Append operations
d.append(4)       # Add to right
d.appendleft(0)   # Add to left
print(f"After appends: {d}")

# Pop operations
right = d.pop()           # Remove from right
left = d.popleft()        # Remove from left
print(f"Popped from right: {right}")
print(f"Popped from left: {left}")
print(f"Final deque: {d}")