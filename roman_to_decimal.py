'''
Convert roman numerals back to decimal
'''
roman = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000
}

def RomanToDecimal(number):
    sum = 0 
    # Iterate over the input string
    for i in range(len(number)-1):
        # Compare 2 numbers at each instance 
        left = number[i]  
        right = number[i+1]
        if roman[left] < roman[right]: # if left number < right number Ex: I vs X subtract
            sum -= roman[left]
        else:
            sum += roman[right] # Otherwise the sum gets the right number value
            
    sum += roman[number[-1]]
    return sum

x = input("Enter a roman numerial: ")
print(RomanToDecimal(x))