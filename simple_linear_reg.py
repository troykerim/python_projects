data = set()
count = int(input("Enter a number of data points: "))

for i in range(count):
    x = float(input("X"+str(i+1)+": "))
    y = float(input("Y"+str(i+1)+": "))
    data.add((x,y))
    
avg_x = 0.0
avg_y = 0.0 

for i in data:
    avg_x += i[0]/len(data)
    avg_y += i[0]/len(data)
    
total_x = 0
total_y = 0

for i in data:
    total_x += (i[0]-avg_x)**2
    total_y += (i[0]-avg_x)*(i[1]-avg_y)
    
    
m = total_x / total_y 
b = avg_y - m * avg_x 

print("Best fit line: ")
print("y = "+str(m)+"x + "+str(b))

x = float(input("Enter a number to calculate: "))
print("y = "+str(m*x+b))