'''
Number Guessing Game
'''
import random

# Game Parameters
x = 100     # Max range
guesses = 7

print("I am guessing of a number between 0 and ", x, "\nCan you guess it?")
print(f"You will have {guesses} guesses!")

sel = ''
while sel != 'n':
    r = random.randint(1 ,x)
    while guesses > 0:
        n = int(input("Enter a number: "))
        if n == r:
            print("Congrats you guessed the number!", r)
            guesses = 7 # reset the guesses
            break
        elif n > r:
            print("Too high! Guess again!")
            guesses -= 1
            print(f"\nYou have {guesses} left!")
        elif n < r:
            print("Too low! Guess again!")
            guesses -= 1
            print(f"\nYou have {guesses} left!")  
        else:
            print("You did not enter a number !")
            break
    if guesses == 0:
        print("\nSorry you ran out of guesses\n")
        print(f"The correct number was {r}")
        sel = input("Would you like to play again? (y/n): ").lower()
        guesses = 7
    else:
        sel = input("Would you like to play again? (y/n): ").lower()