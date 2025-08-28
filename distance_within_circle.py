import math 
# Creating the circle:
# 1. Center coords.  (xcenter, ycenter)
xc = 0
yc = 0  
# 2. Define a radius
r = 3 

# Does the point lie within the circle  
print("Does your point lie within the circle?")
print(f"The circle is centered at between your coords:({xc},{yc}) and the radius is: {r}")
x = int(input("Enter X coord: "))
y = int(input("Enter y coord: "))

# Using distance formula d = sqrt((x1-x2)^2 + (y1-y2)^2)
d = ((x-xc)^2)+((y-yc)^2)
dsqrt = math.sqrt(d)

print(f"\nThe distance between your coords:({x},{y}) and the circle's center:({xc},{yc}) was {dsqrt:.2f}\n")

if dsqrt > r:
    print("Your point lies outside of the circle!")
elif dsqrt < r: 
    print("Your point lies inside of the circle!")
else:
    print("Your point lies on the circle!")