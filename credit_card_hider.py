# Credit card hider
cc = ''

print("Enter your credit card below")
for i in range(16):
    i = input(f"Enter digit number {i+1}: ")[0]
    cc = cc + i 
print(cc)
print(cc[12:])
print("XXXX-XXXX-XXXX-" + cc[12:])
