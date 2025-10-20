from collections import deque

# Implementing a queue (FIFO) with deque
queue = deque()
print("Queue Operations (FIFO):")
# Enqueue operations
queue.append('apple')
queue.append('banana')
queue.append('cherry')
print(f"Queue after enqueuing: {queue}")

# Dequeue operations
first_item = queue.popleft()  # FIFO: first in, first out
print(f"Dequeued first item: {first_item}")
print(f"Queue after dequeuing: {queue}")

# Implementing a stack (LIFO) with deque
stack = deque()
print("\nStack Operations (LIFO):")
# Push operations
stack.append(1)
stack.append(2)
stack.append(3)
print(f"Stack after pushing items: {stack}")

# Pop operations
last_item = stack.pop()  # LIFO: last in, first out
print(f"Popped last item: {last_item}")
print(f"Stack after popping: {stack}")

# Bounded history example with maxlen
history = deque(maxlen=3)
actions = ["open file", "edit content", "save file", "close file"]
for action in actions:
  history.append(action)
print(f"\nLimited history (latest 3 actions): {history}")