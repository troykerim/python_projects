'''
Find the factors of a number.
'''
import math 

def factor(n):
    factor_list = []       # Store all posible factors 
    s = int(math.sqrt(n))   # take the sqrt of input number
    for i in range(1, s+1):  
        if n % i == 0:              # if the remainder of n at the ith number is 0, that is a factor
            factor_list.append(i)
            if i != n // i:          # To avoid duplication
                factor_list.append(n // i)
    factor_list.sort()
    
    return len(factor_list), factor_list

print("Let's find the factors for a particular number.")
n = int(input("Enter a number: "))

factor_count, factors = factor(n)
print(f"\nThere are {factor_count} possible factors for {n}")
print(f"Here are all the factors: {factors}")