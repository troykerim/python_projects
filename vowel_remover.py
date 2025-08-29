# Write a script that takes a user's name and removes all vowels before reversing it.

# 1. Take user's name
name = input("Enter your full name: ")

# 2. Define vowels
vowels = "AEIOUaeiou"

# 3. Remove vowels
no_vowels = "".join([char for char in name if char not in vowels])

# 4. Reverse the string
result = no_vowels[::-1]

print("Modified name:", result)