'''
Least Common Multiple
This version uses a list comparison
'''
def multiples(n, count):
    # Generate a list of multiples for n 
    return [n * i for i in range(1, count + 1)]

def lcm(list1, list2):
    multiple = set(list1) & set(list2)
    return min(multiple) if multiple else None # Return the smallest LCM

print("Least Common Multiple for 2 numbers")
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

# Generate n multiples
n = 20 
mult_a = multiples(a, n) 
mult_b = multiples(b, n)

print(f"\nHere are multiples of {a}: {mult_a}")
print(f"And here are multiples of {b}: {mult_b}")

result = lcm(mult_a, mult_b)
print(f"\nThe least common multiple of {a} and {b} is: {result}")