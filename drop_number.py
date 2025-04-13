'''
drop numbers from a list that are less than the preceding numbers.
'''
def drop(n):
    drop_indices = []
    new_n = [n[0]]
    for i in range(1, len(n)):
        if n[i] < n[i-1]:
            drop_indices.append(i)
        else:
            new_n.append(n[i])
    return drop_indices, new_n

usr_input = input("Enter a list of numbers separated by spaces: ")
n = list(map(int, usr_input.split()))

print("Original list: ",n)
drop_indices, new_n = drop(n)
print("Here are the indices that were dropped: ", drop_indices)
print("New list: ",new_n)