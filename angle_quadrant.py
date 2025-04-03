'''
Angle quadrant checker
'''

def find_quadrant(angle):
    angle = angle % 360
    
    if 0 <= angle <= 90:
        return "First quadrant"
    elif 90 < angle <= 180:
        return "Second quadrant"
    elif 180 < angle <= 270:
        return "Third quadrant"
    elif 270 < angle <= 360:
        return "Forth quadrant"
    else:
        return "Error: Angle out of range"
    
    

angle = int(input("Enter an angle: "))
quadrant = find_quadrant(angle)

print(f"The angle {angle} is in the {quadrant}")