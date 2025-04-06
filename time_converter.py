'''
Basic Time converter

V1 - User enters number of minutes and the program displays different units of time
This can be expanded to allow the user to select other time units instead of minutes
'''

def convert_time(x):
    ns = x * 6e10  # nanoseconds
    mus = x * 6e7  # Microseconds
    ms = x * 60000 # Miliseconds
    s = x * 60     # seconds
    hours= x / 60
    days = x / 1440
    weeks = x / 10080
    months = x / 43800
    print(f"{ns:.2f} nanosecond")
    print(f"{mus:.2f} microsecond")
    print(f"{ms:.2f} milisecond")
    print(s, "seconds")
    print(f"{hours:.2f} hours")
    print(f"{days:.2f} days")
    print(f"{weeks:.2f} weeks")
    print(f"{months:.2f} months")

print("Time converter for minutes")
x = int(input("Enter the number of minutes and let's convert it into different time units: "))
convert_time(x)