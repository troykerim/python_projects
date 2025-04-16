def triangle(sides):
    a, b, c = sorted(sides)
    s = sum(sides) / 2 
    
    area = (s * (s-a) * (s-b) * (s-c)) ** 0.5
    
    y = 2 * area / a
    x = (c ** 2 - y ** 2) ** 0.5
    return [[0.0, 0.0] , [a, 0.0], [x,y]]
    
user_input = input("Enter elements separated by commas: ")
sides = list(map(int, user_input.split(',')))

print(triangle(sides))