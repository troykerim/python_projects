'''
Unit Converter 
'''

def inches2metric(num):
    cm = num * 2.54 
    meter = num / 39.37
    km = num / 39370
    print("Your number in centimeters:" ,cm, "cm")
    print(f"Your number in meters: {meter:.2f}m")
    print(f"Your number in kilometers: {km:.4f}km")

def feet2metric(num):
    cm = num * 30.48
    meter = num / 3.281 
    km = num / 3281 
    print("Your number in centimeters: ", cm, "cm")
    print(f"Your number in meters: {meter:.2f}m")
    print(f"Your number in kilometers: {km:.4f}km")
    
def miles2metric(num):
    cm = num * 160900
    meter = num * 1609
    km = num * 1.609 
    print("Your number in centimeters:", cm, "cm")
    print(f"Your number in meters: {meter:.2f}m")
    print(f"Your number in kilometers: {km:.4f}km")
    
def km2imperial(num):
    miles = num / 1.609
    foot = num * 3281 
    inches = num * 39370 
    print("Your number in miles:", miles, "miles")
    print(f"Your number in foot: {foot} ft")
    print(f"Your number in inches: {inches}in")
    
def m2imperial(num):
    miles = num / 1609 
    foot = num * 3.281 
    inches = num * 39.37
    print("You number in miles:", miles, "miles")
    print(f"Your number in foot: {foot} ft")
    print(f"Your number in inches: {inches} in")
    
def cm2imperial(num):
    miles = num / 160900
    foot = num / 30.48
    inches = num / 2.54 
    print("Your number in miles:", miles, "miles")
    print(f"Your number in feet: {foot} ft")
    print(f"Your number in inches: {inches} in")

print("Unit converter")
print("Enter 'm' for Metric or 'i' for Imperial?")
choice1 = input('>').lower()

if choice1 == 'm':
    choice2 = input('> ').lower()
    print("Which unit are you converting: 'k' for kilometers, 'm' for meter, 'c' for centimeters?")
    if choice2 == 'i':
        num = float(input("Enter your number in (kilometers): "))
        km2imperial(num)
    elif choice2 == 'f':
        num = float(input("Enter your number in (feet): "))
        m2imperial(num)
    elif choice2 == 'm':
        num = float(input("Enter your number in (miles): "))
        cm2imperial(num)
    else:
        print("You did not enter the correct choice!")
elif choice1 == 'i':
    choice2 = input('> ').lower()
    print("Which unit are you converting: 'k' for kilometers, 'm' for meter, 'c' for centimeters?")
    if choice2 == 'i':
        num = float(input("Enter your number in (kilometers): "))
        inches2metric(num)
    elif choice2 == 'f':
        num = float(input("Enter your number in (feet): "))
        feet2metric(num)
    elif choice2 == 'm':
        num = float(input("Enter your number in (miles): "))
        miles2metric(num)
    else:
        print("You did not enter the correct choice!") 
else:
    print("You did not enter the correct choice!")