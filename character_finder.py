# Key character finder from a input string
from collections import Counter 

most_freq = input("Enter text: ")

# Count each character occurance 

count = dict(Counter(most_freq))

char_find = input("Enter a character to search for: ")

if char_find in count:
    print(f"The character {char_find} appears {count[char_find]} times")
else:
    print(f"The character {char_find} was not found.")
