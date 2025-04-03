'''
Decimal to Binary Converter
'''
def dec2bin(x: int) -> str:
    result = ""
    if x == 0:
        return "0" # if the user inputs  0
    while(x > 0):
        result = str(x % 2) + result
        x //= 2
        
    return result

x = int(input("Enter a whole number to be converted to binary: "))

result = dec2bin(x)
print(result)

# Alternate version
'''
print(f"The result is {result}")
def convert2Bin(y):
    if y > 1:
        convert2Bin(y//2)
    print(y % 2)

y = int(input("Enter another number: "))
print(convert2Bin(y))

print(bin(100))'''