class Node:
    def __init__(self):
        self.data = 0 
        self.next = None
        self.child = None 
        
def createList(arr, n):
    head = None
    temp = None 
    
    for i in range(n):
        if(head == None):
            temp = head = Node()
        else:
            temp.next = Node() 
            temp = temp.next 
            
        temp.data = arr[i]
        temp.next = temp.child = None 
    return head

def printList(head):
    while(head != None):
        if(head.child != None):
            printList(head.child)
        print(head.data, end=' ')
        head = head.next 
    # print()
        
if __name__ == '__main__':
    arr1 = [1,2,3]
    arr2 = [5,6]
    arr3 = [4]
    arr4 = [7, 8, 9]
    
    head1 = createList(arr1, 3)
    head2 = createList(arr2, 2)
    head3 = createList(arr3, 1)
    head4 = createList(arr4, 3) 
    
    head1.child = head2
    head1.next.next.child = head3 
    head2.next.child = head4 
    
    head = None 
    head = head1 
    printList(head)