"""
    Stack implementation using an Array/list (Dynamically)
    
    Implements the 5 of the basic opperation:
    
    push() to insert an element into the stack
    pop() to remove an element from the stack
    top() Returns the top element of the stack.
    isEmpty() returns true if stack is empty else false.
    size()  return the length/size of stack
    
    isFull() is not used, but would be implemented if working with a static array and would check if the size of the array was maxed out.
"""

class Stack:
    def __init__(self):
        self.stack = []   # Create an empty stack array 
    
    def push(self, n):
        self.stack.append(n)  # Insert a number into the stack 
        
    def pop(self):
        if self.isEmpty():
            return "Stack is Empty"
        # return self.stack.pop() # pop() is a built-in python function
        # Long way to remove an element:
        top_element = self.stack[-1] 
        self.stack = self.stack[:-1]
        return top_element 
    
    
    def top(self):  # AKA Peek, check top of stock, basically check last element in array
        if self.isEmpty():
            return "Stack is Empty"
        return self.stack[-1]
    def isEmpty(self):
        return len(self.stack) == 0
    def size(self):
        return len(self.stack)


def main():
    print("Stack Data Structure Tester")
    # Create a stack
    stack = Stack()

    while True:
        print("\nChoose an operation:")
        print("1. Push value")
        print("2. Pop value")
        print("3. Check Top")
        print("4. Stack size")
        print("5. Print stack contents")
        print("Q. Quit")

        choice = input("\nEnter your choice: ").strip().lower()

        if choice == '1':
            val = int(input("Enter value to push: "))
            stack.push(val)
            print(f"Value {val} added.")
            
        elif choice == '2':
            if stack.size() == 0:
                print("Stack is empty. Nothing to pop.")
            else:
                val = stack.pop()
                print(f"Popped value: {val}")
                
        elif choice == '3':
            if stack.size() == 0:
                print("Stack is empty!")
            else:
                val = stack.top()
                print(f"Top of the stack is: {val}")
                
        elif choice == '4':
            print(f"Current Stack size: {stack.size()}")
            
        elif choice == '5':
            print(f"Current Stack contents: {stack.stack}")
            
        elif choice == 'q':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()