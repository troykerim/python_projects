'''
Basic Dice rolling game
Play against the computer.
You roll a dice and the computer rolls a dice, whoever rolls the highest wins.
'''
import random 

def cpu_roll(x):
    roll = random.randint(1,6)
    print("The CPU rolled a", roll)
    return roll
def user_roll(x):
    roll = random.randint(1,6)
    print("You rolled a", roll)
    return roll    

print("Welcome to the dice rolling game!")
x = int(input("Enter a nubmer of dice you want to roll: "))
cpu_num = 0
user_num = 0 

for i in range(x):
    n = cpu_roll(x)
    cpu_num += n
    m = user_roll(x)
    user_num += m

print("\n")
print("CPU's total is =", cpu_num)
print("User's total is =", user_num)

if cpu_num > user_num:
    print("\nCPU won!")
elif cpu_num < user_num:
    print("\nUser won!")
else:
    print("\nYou both won!")    
    