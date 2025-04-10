'''
Greatest Common Factor - Long way
'''
# Find all the factors of a number and return it as a list
def factor(x, factor_list):
    for i in range(1, x+1):
        if x % i == 0:
            factor_list.append(i)
        # Otherwise, do nothing 
    return factor_list

# Compare the all the factors of both numbers, find which number was the greatest
# The defualt GCF for all numbers is 1
# Ex: GCF for 4 and 7 is going to be 1, because, 4 = [1,2,4] &  7 = [1,7]
def gcf(factor_list1, factor_list2):
    set1 = set(factor_list1)
    set2 = set(factor_list2)
    dup = list(set1.intersection(set2))
    gcf_val = max(dup)
    return gcf_val 

print("Let's find the Greatest Common Factor (GCF of 2 numbers)")
x1 = int(input("Enter a number: "))
x2 = int(input("Enter another number: "))

factor_list1 = []
factor_list2 = []

result1 = factor(x1, factor_list1)
result2 = factor(x2, factor_list2)

print(f"The factors of 1st your number {x1} are: {result1}")
print(f"The factors of 1st your number {x2} are: {result2}")
gcf_val = gcf(factor_list1, factor_list2)
print(f"\nGCF of {x1} and {x2} is: {gcf_val}")