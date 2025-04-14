'''
Pair Sum using 2 pointer techniques
'''

def isPairSum(A, N, X):
    # 1st pointer
    i = 0
    # 2nd pointer
    j = N - 1 # Len of array, starts at the end of the array
    
    while(i < j):
        # If we find a pair
        if(A[i] + A[j] == X):
            return True
        # If the sum of elements at current pointers is less, move towards higher value
        elif(A[i] + A[j] < X):
            i += 1 
        # If sum of elements at currnt possition is more, move towards lower value
        else:
            j -= 1 
    return 0 
    
arr = [3, 5, 9, 10, 2, 10, 8, 11]
val = 17

print(isPairSum(arr, len(arr), val))