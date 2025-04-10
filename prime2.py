import math
def prime(x):
    res = []                                # stores result
    for i in range(2, x+1):                 # Start checking 2 because 0 and 1 are not prime numbers
        for j in range(2, i // 2 + 1):      # For current number i, loop checks all numbers j from 2 to i // 2 (half of i)
            if i % j == 0:                  # If j divides i evenly, then i is not prime
                break
        else:
            res.append(i)
            
    return res 

x = int(input("Enter a number: "))
print(prime(x))