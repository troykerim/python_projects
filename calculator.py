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

while True:    
    print("Selection an option below:")
    print("\nEnter 'a' for addition")
    print("\nEnter 's' for subtract")
    print("\nEnter 'm' for multiplication")
    print("\nEnter 'd' for division")
    choice = input("Your input: ").lower()

    
    try:
        n1 = int(input("Your 1st number: "))
        n2 = int(input("Your 2nd number: "))
    except ValueError:
        print("Invalid number input! Please enter integers.")
        continue

    if choice == 'a':
        result = add(n1,n2)
        print(f"\nResult: {result}")
    elif choice == 's':
        result = sub(n1,n2)
        print(f"\nResult: {result}")
    elif choice == 'm':
        result = mul(n1, n2)
        print(f"\nResult: {result}")
    elif choice == 'd':
        result = div(n1, n2)
        print(f"\nResult: {result}")
    else:
        print("Error, Wrong input!")
    again = input("\nWould you like to perform another calculation? (y/n): ").strip().lower()
    if again != 'y':
        print("Thank you for using the calculator.")
        break