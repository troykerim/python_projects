# Dynamic Array implementation
# Note: Python lists are dynamic arrays by default,
# but this is an example of what's going on under the hood.
class DynamicArray:
    '''
        Contructor
        Predefine the members of the Dynamic array
        length is the size of the array
        Once a size has been passed, the array will be initially all 0s based on the capacity
        Capacity is also dependent on the length.  
        
        In short, create an array of size (length) and initialize the array with all 0s.  
        The array will temporarily not contain any values
    '''
    def __init__(self, capacity: int):
        self.capacity = capacity        # Save the capacity, doing so implements the getCapacity() below
        self.length = 0                 # Initialize the size of the array
        self.arr = [0] * self.capacity # if our array was sized 4, we'd have an array of 4 0s [0, 0, 0, 0]

    '''
        Retrieve an element from the array 
        Get value at i-th index
        Assume i-th index is valid, even if we don't have any values within the array yet,
        because it is implied that this function will only be called with a valid array
    '''
    def get(self, i: int) -> int:
        return self.arr[i]  

    '''
        Add a value into the array, Set n at i-th index
    '''
    def set(self, i: int, n: int) -> None:
        self.arr[i] = n

    '''
        Insert n in the last position of the array
        Increment the array, we don't do it at the insert "set()" because the 
    '''
    def pushback(self, n: int) -> None:
        # If we don't have enough capacity, we will get an out of bounds error
        # Then resize the array, and this function call happens before the insertion
        if self.length == self.capacity:
            self.resize()
            
        # insert at next empty position & increase the size the of the array
        self.arr[self.length] = n       
        self.length += 1    

    '''
        Assume valid, decrement the length of the array by 1
        Return the element that was popped
        We are popping the last element because arrays start at index 0!
        Ex: [1, 2, 3, 4], we would pop 4 and return 4. 
    '''
    # Remove the last element in the array
    def popback(self) -> int:
        if self.length > 0:
            # soft delete the last element
            self.length -= 1
        # return the popped element
        return self.arr[self.length] 

    '''
        Create new array of double capacity
        Called during the pushback()
    '''
    def resize(self) -> None:
        
        self.capacity = 2 * self.capacity
        new_arr = [0] * self.capacity   # Create a new array of size capacity; will contain all 0s right now
        
        # Copy elements to new_arr
        for i in range(self.length):
            new_arr[i] = self.arr[i]
        self.arr = new_arr

    def getSize(self) -> int:
        return self.length
    
    def getCapacity(self) -> int:
        return self.capacity        # collects that value that was stored in capacity in the contructor


'''
    Test function and covers each function operation.
'''
def main():
    print("Dynamic Array Test Interface")
    arr = DynamicArray(capacity=2)  # Start small to test resizing

    while True:
        print("\nChoose an operation:")
        print("1. Push back")
        print("2. Pop back")
        print("3. Get value at index")
        print("4. Set value at index")
        print("5. Get size")
        print("6. Get capacity")
        print("7. Print array contents")
        print("Q. Quit")

        choice = input("\nEnter your choice: ").strip().lower()

        if choice == '1':
            val = int(input("Enter value to push: "))
            arr.pushback(val)
            print(f"Value {val} added.")
        elif choice == '2':
            if arr.getSize() == 0:
                print("Array is empty. Nothing to pop.")
            else:
                val = arr.popback()
                print(f"Popped value: {val}")
        elif choice == '3':
            i = int(input("Enter index to get: "))
            if 0 <= i < arr.getSize():
                print(f"Value at index {i}: {arr.get(i)}")
            else:
                print("Index out of bounds.")
        elif choice == '4':
            i = int(input("Enter index to set: "))
            if 0 <= i < arr.getSize():
                val = int(input("Enter new value: "))
                arr.set(i, val)
                print(f"Value at index {i} set to {val}.")
            else:
                print("Index out of bounds.")
        elif choice == '5':
            print(f"Current size: {arr.getSize()}")
        elif choice == '6':
            print(f"Current capacity: {arr.getCapacity()}")
        elif choice == '7':
            print("Array contents:")
            for i in range(arr.getSize()):
                print(f"[{i}] = {arr.get(i)}")
        elif choice == 'q':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()