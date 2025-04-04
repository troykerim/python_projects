'''
Element counter in 2 forms 

First part, asks user to enter elements into a list and then asks for a specific element and checks if that element appeared in their list
Second part, creates a list of random elements valued between 0 and 100.  User is asked to see if their number appeared in that list
'''

import random
def count(a, b):
    # a is the original list 
    # b is the value you want to find
    count = 0
    for i in a:
        if (i == b):
            count = count + 1 
    if count == 0:
        return 0
    else:
        return count 

a = []

x = int(input("How big do you want your list: "))
for i in range(x):
    w = int(input(f"Enter element number {i+1}: "))
    a.append(w)

print("Here is your list: ")
print(a)

b = int(input("Enter a number and let's see how many times it appeared: "))
result = count(a,b)
print(f"The number {b} appeared {result} times.")

c = [random.randint(1, 100) for _ in range(20)]
print(c) 
result = count(c, b)
print(f"The number {b} appeared {result} times.")
print(c)