'''
Number of students eating.  Leetcode 

'''
from collections import Counter
def countStudents(students, sandwiches):
    res = len(students)
    count = Counter(students)
    
    for s in sandwiches:
        if count[s] > 0:
            res -= 1
            count[s] -= 1
        else:
            break
    return res 

