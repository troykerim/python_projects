'''
Design a stack class that supports the push, pop, top, and getMin operations.

    MinStack() initializes the stack object.
    void push(int val) pushes the element val onto the stack.
    void pop() removes the element on the top of the stack.
    int top() gets the top element of the stack.
    int getMin() retrieves the minimum element in the stack.
'''

class MinStack:
    min = float('inf')
    def __init__(self):
        self.stack = []
        self.min=float('inf')

    def push(self, val: int) -> None:
        if val <= self.min:
            self.stack.append(self.min)
            self.min = val
        self.stack.append(val)

    def pop(self) -> None:
        t = self.stack[-1]
        self.stack.pop()
        if self.min == t:
            self.min = self.stack[-1]
            self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min
    
    
# Function to test the Stack Class
def test_MinStack(ops, values):
    obj = None
    results = []

    for i in range(len(ops)):
        if ops[i] == "MinStack":
            obj = MinStack()
            results.append(None)
              
        elif ops[i] == "push":
            obj.push(values[i])
            results.append(None)
            
        elif ops[i] == "pop":
            obj.pop()
            results.append(None)
            
        elif ops[i] == "top":
            results.append(obj.top())
            
        elif ops[i] == "getMin":
            results.append(obj.getMin())
            
    return results


ops = ["MinStack", "push", "push", "push", "getMin", "pop", "top", "getMin"]
values = [None, 1, 2, 0, None, None, None, None]

output = test_MinStack(ops, values)
print(output)