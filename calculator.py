def add(a, b):
    return a + b
def sub(a, b):
    return a - b 
def mul(a, b):
    return a * b 
def div(a, b):
    if a == 0 or b == 0:
        return print("ERROR! Cannot Divide by 0!")
    else:
        return a / b 
    
print("Welcome to the calculator")
print("Use 2 numbers.")

print("Selection an option below:")
print("\nEnter 'a' for addition")
print("\nEnter 's' for subtract")
print("\nEnter 'm' for multiplication")
print("\nEnter 'd' for division")

choice = input("Your input: ").lower()
n1 = int(input("Your 1st number: "))
n2 = int(input("Your 2nd number: "))

if choice == 'a':
    print("\n", add(n1, n2))
elif choice == 's':
    print("\n", sub(n1,n2))
elif choice == 'm':
    print("\n", mul(n1,n2))
elif choice == 'd':
    print("\n", div(n1,n2))
else:
    print("Error, Wrong input!")