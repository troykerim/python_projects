'''
Generate multiples for a number using recursion
'''
def multiples(n, m, current = 1, result = None):
    # Generate a list of of m multiples for a number n.
    if result is None:
        result= []
    if current > m:
        return result 
    result.append(n*current)
    return multiples(n, m, current+1, result)

print("Multiples generator")
a = int(input("Enter a number: "))
b = int(input("How many multiples of would like?: "))

result = multiples(a,b)
print(f"The multiples of {a} are {result}")

