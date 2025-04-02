
# Convert degrees to radians
def deg2rad(x: float) -> float:
    result = (3.14/180) * x
    return result 
# Convert radians to degrees 
def rad2deg(x: float) -> float:
    result = (180/3.14) * x 
    return result 

print("Degrees or Radians?")
sel = input("Enter 'd' for degrees or 'r' for radians: ").lower()
if sel == 'r':
    x = float(input("Enter your angle: "))
    print("\nConverting degrees to radians!\n")
    result = deg2rad(x)
    print(f"Your angle {x:.2f} in degrees is: {result:.3f} radians")
    
elif sel == 'd':
    x = float(input("Enter your angle: "))
    print("\nConverting radians to degrees!\n")
    result = rad2deg(x)
    print(f"Your angle {x:.2f} in radians is: {result:.3f} degrees") 
else:
    print("Invalid input!")