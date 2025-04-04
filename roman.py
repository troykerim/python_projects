def roman_ones(n):
    ones = {1: "I", 2: "II", 3: "III", 4: "IV", 5: "V", 6: "VI", 7: "VII", 8: "VIII", 9: "IX"}
    return ones.get(n, "")

def roman_tens(n):
    tens = {1: "X", 2: "XX", 3: "XXX", 4: "XL", 5: "L", 6: "LX", 7: "LXX", 8: "LXXX", 9: "XC"}
    return tens.get(n, "")

def roman_hundreds(n):
    hundreds = {1: "C", 2: "CC", 3: "CCC", 4: "CD", 5: "D", 6: "DC", 7: "DCC", 8: "DCCC", 9: "CM"}
    return hundreds.get(n, "")

def roman_thousands(n):
    thous = {1: "M", 2: "MM", 3: "MMM"}
    return thous.get(n, "")

print("Roman Numeral Converter")
n = int(input("Enter a number: "))
thous = (n // 1000) % 10 
huns = (n // 100) % 10 
tens = (n // 10) % 10 
ones = n % 10 

print(f"Hundreths: {huns}, Tens: {tens}, Ones: {ones}")
roman_numeral = roman_thousands(thous) + roman_hundreds(huns) + roman_tens(tens) + roman_ones(ones)
print(f"Your number {n} in roman numbers is: {roman_numeral}")