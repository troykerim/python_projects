# Write a Python program that accepts a full name and prints the initials in uppercase.

def find_initials(name):
    # Create an empty list to store all capital letters found
    initials = []
    # Scan over the input string and check if a char is capitalized
    for char in name:
        if char.isupper():
            initials.append(char)
    
    if not initials:
        return "No capital letters were found!"
    return initials
    
    
name = input("Enter your full name: ")

initials = find_initials(name)
print(f"Here are your intials: {initials}")