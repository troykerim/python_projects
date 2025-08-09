'''
    Linked List implementation
    
    Search for an element in a linked list (singly)
'''

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
# Find if a target value is present in a linked list
def search(head, target):
    curr = head  # Start at the head of the list
    
    while curr is not None:
        if curr.data == target:  # Found the target
            return True
        curr = curr.next  # Move to next node
    
    return False  # Target not found


def traverseList(head):
    while head is not None:
        print(head.data, end=' ')
        head = head.next
    print()


def main():
    head = None
    tail = None

    print("Enter values for the linked list. Press Q to quit.")

    while True:
        val = input("Enter a number (or Q to quit): ").strip()
        if val.lower() == 'q':
            break
        
        try:
            num = int(val)
        except ValueError:
            print("Please enter a valid integer or Q to quit.")
            continue

        new_node = Node(num)

        if head is None:
            head = new_node
            tail = new_node
        else:
            tail.next = new_node
            tail = new_node

    if head is None:
        print("\nLinked list is empty.")
        return

    print("\nLinked List contents:")
    traverseList(head)

    # Ask for target value
    try:
        target = int(input("Enter the value to search for: "))
    except ValueError:
        print("\nInvalid input. Must be an integer.")
        return

    if search(head, target):
        print(f"\nThe value {target} was found in the linked list.")
    else:
        print(f"\nThe value {target} was not found in the linked list.")


if __name__ == "__main__":
    main()
