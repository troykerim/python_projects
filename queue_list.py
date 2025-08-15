'''
    Queue Implementation as Python list
    
    Queue = FIFO (First In First Out)
    
'''

class Queue:
    def __init__(self):
        self.queue = []
        
    # Push data to the queue
    def enqueue(self, data):
        self.queue.append(data)
    
    # Pop data from the queue
    def dequeue(self):
        if self.isEmpty():
            return "Queue is empty!"
        return self.queue.pop(0) # Pop the very first element
    
    # Check the top element of the queue
    def peek(self):
        if self.isEmpty():
            return "Queue is empty!"
        return self.queue[0]
    
    def isEmpty(self):
        return len(self.queue) == 0
    
    def size(self):
        return len(self.queue)
    
myQueue = Queue()

print("Is the Queue empty?", myQueue.isEmpty())
print("Queue size: ", myQueue.size())

myQueue.enqueue(1)
myQueue.enqueue(2)
myQueue.enqueue(3)
print("Current Queue: ", myQueue.queue)

print("Is the Queue empty?", myQueue.isEmpty())
print("Queue size: ", myQueue.size())

print("Removing an element: ", myQueue.dequeue())
print("Current Queue: ", myQueue.queue)
print("Is the Queue empty?", myQueue.isEmpty())
print("Queue size: ", myQueue.size())

