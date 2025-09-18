from collections import OrderedDict

# Define a class 'LRUCache' for a Least Recently Used (LRU) cache
class LRUCache:
    # Initialize the LRUCache with a specified capacity
    def __init__(self, capacity: int):
        # Create an ordered dictionary 'cache' to store key-value pairs
        self.cache = OrderedDict()
        # Set the capacity of the cache
        self.capacity = capacity

    # Get the value associated with a key from the cache
    def get(self, key: int) -> int:
        # Check if the key is not in the cache
        if key not in self.cache:
            return -1
        else:
            # Move the accessed key to the end to mark it as most recently used
            self.cache.move_to_end(key)
            # Return the value associated with the key
            return self.cache[key]

    # Put a key-value pair into the cache
    def put(self, key: int, value: int) -> None:
        # Update the cache with the key-value pair
        self.cache[key] = value
        # Move the key to the end to mark it as most recently used
        self.cache.move_to_end(key)
        # Check if the cache size exceeds the specified capacity
        if len(self.cache) > self.capacity:
            # Remove the least recently used item (the first item) from the cache
            self.cache.popitem(last=False)

# Create an instance of the LRUCache class with a capacity of 2
cache = LRUCache(2)

# Put key-value pairs into the cache
cache.put(10, 10)
cache.put(20, 20)

# Get the value associated with key 10 from the cache
print(cache.get(10))   # 10

# Put another key-value pair into the cache, which causes the eviction of the least recently used item (key 20)
cache.put(30, 30)

# Get the value associated with key 20, which is not in the cache
print(cache.get(20))   # -1 

# Put another key-value pair into the cache, which causes the eviction of the least recently used item (key 10)
cache.put(40, 40)

# Get the value associated with key 10, which is not in the cache
print(cache.get(10))   # -1 

# Get the values associated with keys 30, and 40 from the cache
print(cache.get(30))   # 30
print(cache.get(40))   # 40 