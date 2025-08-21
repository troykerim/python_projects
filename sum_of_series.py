'''
Sum of series n + (n-2) + (n-4) positive integers

until n-x =< 0
'''
    
# Recursive
def sum(n):
    if n < 1:
        return 0
    else:
        return n + sum(n-2)
        
# Iterative
def sum_1(n):
    total = 0
    while n > 0:
        total += n
        n -= 2
    return total

print(sum(6))

print(sum_1(6))