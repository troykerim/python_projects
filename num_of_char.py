"""
Number of character occurances using the counter module
"""

from collections import Counter 
most_freq = input("Enter text: ")
count = dict(Counter(most_freq))
print("Character count: ", count)

