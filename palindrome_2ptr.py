'''
Palindrome problem using 2 pointers
'''

def isPalindrome(s):
    l = 0  # left pointer
    r = len(s) - 1 # right pointer
    while(l < r):
        if s[l] != s[r]:   # Check the index for s and if the don't match, Not a palidrome
            return False
        l += 1 
        r -= 1 
    return True 

s = input("Enter a word: ")
print(isPalindrome(s))