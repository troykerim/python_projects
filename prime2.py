import math
def prime(x):
    res = []
    for i in range(2, x+1):
        if i <= 1:
            continue
        for j in range(2, i // 2 + 1):
            if i % j == 0:
                break
        else:
            res.append(i)
            
    return res 

x = int(input("Enter a number: "))
print(prime(x))