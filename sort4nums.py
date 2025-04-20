a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
d = int(input("Enter fourth number: "))

first = min(a, b, c, d)  # Smallest number
last = max(a, b, c, d)   # Largest number

# Sum of all numbers minus smallest and largest gives the two middle numbers' sum
middle_sum = (a + b + c + d) - first - last 

# Use min() to find the smaller middle number
second = min(a, b, c, d, key=lambda x: abs(x - middle_sum // 2))

# The remaining number is the third number
third = middle_sum - second

# Print the sorted numbers
print("Sorted numbers:", first, second, third, last)