'''
Greatest Common Factor - Shorter way
'''

# Using recursion and Euclid algorithm

def gcf(a, b):
    # Base case 
    if b == 0:
        return a
    else:
        return gcf(b, a % b)
    
print("Greatest Common Factor")
a = int(input("Enter a number: "))
b = int(input("Enter another number: "))

print(f"The greatest common factor of {a} and {b} is {gcf(a,b)}")