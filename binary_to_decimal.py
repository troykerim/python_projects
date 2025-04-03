# Binary to decimal converter
def bin2dec(x: int) -> int:
    decimal = 0 # store final result
    power = 0 # keep track of digit position from right to left starting at 0
     
    for digit in reversed(binary): # process from right side and not left side
        if digit not in ('0', '1'):
            raise ValueError("Invalid binary string")
        decimal += int(digit) * 2**power
        power += 1 
    return decimal

binary = input("Enter a binary number: ")
try:
    decimal = bin2dec(binary)
    print("The decimal value is: ", decimal)
except ValueError as e:
    print("Error: ", e)