'''
Debt calculator - work in progress
'''
import math 
def debt(d, m, i):
    # for _ in range(m):
    d *= (1 + i) ** m
    d = math.ceil(d / 1000) * 1000 
    return int(d)

d = int(input("Enter the amount of debt: "))
m = int(input("Enter the number of months: "))
i = float(input("Enter the interest amount (Ex: 0.05 = 5%): "))

final_debt = debt(d, m, i)
print(f"THe amount of debt you would owe in {m} months at {i} interest is: ${final_debt}")