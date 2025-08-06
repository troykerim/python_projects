'''
    Valid Parentheses
    
    Given a string consisting of characters: ( ) [ ] { }, check for valid input if and only if:
    1. Every open bracket is closed by the same type
    2. Open brackets are closed in the correct order
    3. Every closed bracket has a corresponding open bracket of the same type.
    
    Input: s = "[]"
    Output: True
    Input: s = "[()]"
    Output: True
    Input: s = "((({})))"
    Output: True
    Input: s = "]()"
    Output: False
'''


def isValid(s: str) -> bool:
    # Create an empty stack to check string 
    stack = []
    closeToOpen = {')':'(', '}': '{', ']':'['} # Dict to map close brackets to open brackets
    
    for c in s:
        if c in closeToOpen:                            # Check if the character in the string matches the a value in the dictionary
            if stack and stack[-1] == closeToOpen[c]:   # Check if we have an empty stack and if the top of the stack contains an open bracket
                stack.pop() 
            else:
                return False                            # pop the stack if we find a match (), [], or {} if we don't find a match, we know the string is invalid
        else:
            stack.append(c)                             # append the stack with open brackets and if a closed bracket is found, execute inner if/else
    return True if not stack else False                 # If the stack is empty, we found all the matchs and string was valid.  


s1 = "[]"
print(isValid(s1))

s2 = "[[]"
print(isValid(s2))

s3 = "[[()]]"
print(isValid(s3))

s4 = "{[[()]]}"
print(isValid(s4))

s5 = ")(()))"
print(isValid(s5))