print("Welcome to the Age Calculator")
print("Let's see how old you really are\n")

age = int(input("Enter your age (years only): "))
days = age * 365
months = age * 12 
weeks = age * 52.143
decades = age / 10 
minutes = age * 525600
seconds = age * 3.154E7

print(f"Your age in {seconds} seconds")
print(f"Your age in {minutes} minutes")
print(f"Your age in {days} days")
print(f"Your age in {months} months")
print(f"Your age in {weeks:.2f} weeks")
print(f"Your age in {decades:.1f} decades")

