class FIFO:
    def __init__(self, capacity=20):
        self.queue = [None] * capacity
        self.capacity = capacity
        self.front = 0
        self.rear = -1
        self.size = 0

    def is_full(self):
        return self.size == self.capacity

    def is_empty(self):
        return self.size == 0

    def enqueue(self, value):
        if self.is_full():
            print("FIFO is full. Cannot add more elements.")
            return
        self.rear = (self.rear + 1) % self.capacity
        self.queue[self.rear] = value
        self.size += 1
        print(f"Added '{value}'. Space left: {self.capacity - self.size}")

    def dequeue(self):
        if self.is_empty():
            print("FIFO is empty.")
            return None
        value = self.queue[self.front]
        self.queue[self.front] = None
        self.front = (self.front + 1) % self.capacity
        self.size -= 1
        print(f"Removed '{value}'")
        return value

    def peek_front(self):
        if self.is_empty():
            print("FIFO is empty.")
        else:
            print(f"Front (oldest): {self.queue[self.front]}")

    def peek_rear(self):
        if self.is_empty():
            print("FIFO is empty.")
        else:
            print(f"Rear (newest): {self.queue[self.rear]}")

    def clear(self):
        self.queue = [None] * self.capacity
        self.front = 0
        self.rear = -1
        self.size = 0
        print("FIFO cleared.")


fifo = FIFO()

print("FIFO Queue - Interactive Mode")
print("Commands:")
print("1: Enqueue")
print("2: Dequeue")
print("3: Peek Front")
print("4: Peek Rear")
print("5: Clear FIFO")
print("6: Exit")

while True:
    cmd = input("\nEnter command number: ")

    if cmd == '1':
        if fifo.is_full():
            print("FIFO is full. Cannot add more.")
        else:
            value = input("Enter value to enqueue: ")
            fifo.enqueue(value)
    elif cmd == '2':
        fifo.dequeue()
    elif cmd == '3':
        fifo.peek_front()
    elif cmd == '4':
        fifo.peek_rear()
    elif cmd == '5':
        fifo.clear()
    elif cmd == '6':
        print("Exiting.")
        break
    else:
        print("Invalid command. Please enter a number from 1 to 6.")

