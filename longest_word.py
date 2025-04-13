'''
Find the longest word from a list of word
'''

def longest_str(n):
    return max(n, key=len)

words = input("Enter words seperated by a comma: ")
n = words.split(',')

print("The longest word in your input was: ", longest_str(n))