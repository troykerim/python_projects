'''
Fibonacci sequence using a while loop
'''
print("Fibonacci sequence")
n = int(input("Enter a number: "))

# Base cases 
n1 = 0
n2 = 1 
next_num = n2 
count = 1 
while count <= n:
    print(next_num, end=' ')
    count += 1
    n1, n2= n2, next_num # update base variables
    next_num = n1 + n2
print()