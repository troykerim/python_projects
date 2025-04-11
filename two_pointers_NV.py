# Naive approach for two pointers/two sum problem

def isPairSum(A, N, X):
    for i in range(N):
        for j in range(N):
            if(i == j):
                continue 
            if(A[i] + A[j] == X):
                return True
            if(A[i] + A[j] > X):
                break
    return 0 

arr = [0, 3, 1, 50, 18, 9, 11, 32, 13]
target = 9 
print(isPairSum(arr, len(arr), target))         