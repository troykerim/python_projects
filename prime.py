import math
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True


print("Prime number checker!")
x = int(input("Enter a number and lets see if it's prime or not: "))
print(is_prime(x))

'''
for x in range(1,x+1):
    print("The number ", x, " as a prime number is ", is_prime(x))'''