# Write a script that finds the nearest multiple of 100 for a given number.
import math
def multiple(n, mult):
    if mult == 0:
        return 0 
    # return mult * round(n/mult) # Will round down
    return mult * math.floor((n + mult/2) / mult)

n = int(input("Enter a number: "))
mult = 100
nearest = multiple(n, mult)
print(f"The nearest multiple of {mult} to {n} is: {nearest}")