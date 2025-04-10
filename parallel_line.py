"""
Parallel line checker
"""
print("Parallel line checker.")
print("Enter 4 (x,y) data points below.")
x1, y1 = map(float, input("Datapoint1: ").split())
x2, y2 = map(float, input("Datapoint2: ").split())
x3, y3 = map(float, input("Datapoint3: ").split())
x4, y4 = map(float, input("Datapoint4: ").split())

# slope = (x2 - x1) / (y2 - y1) 

try:
    slope1 = (y2-y1) / (x2-x1)
    slope2 = (y4-y3) / (x4-x3)
    if slope1 == slope2:
        print("The lines are parallel!")
    else:
        print("The lines are not parallel!")
except ZeroDivisionError:
    print("Error: One of the lines is vertical (undefined slope).")