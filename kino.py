# Kino Machine 


'''
Modify this code so that...
CPU picks 20 numbers 
User only picks up to 5-10 numbers.
If they get numbers that match increase the reward.

'''
import random

def number_gen(x: int) -> list[int]:
    """Generates a list of unique random numbers between 0 and 99."""
    rand_set = set()
    while len(rand_set) < x:
        num = random.randint(0, 99)
        rand_set.add(num)
    return list(rand_set)

def user_input(nums_to_gen: int) -> list[int]:
    """Prompts the user to enter a list of unique numbers between 0 and 99."""
    user_nums = []
    print("\nNow pick your numbers!")
    print(f"You need to pick {nums_to_gen} numbers.")
    while len(user_nums) < nums_to_gen:
        try:
            user_number = int(input(f"Enter a number {len(user_nums) + 1}: "))
            if 0 <= user_number <= 99:
                if user_number in user_nums:
                    print("That number has already been picked. Please enter a different number!")
                else:
                    user_nums.append(user_number)
            else:
                print("Number out of range. Please enter a number between 0 and 99.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    return user_nums

def comparison(cpu_nums: list[int], user_nums: list[int]) -> int:
    """Compares two lists and returns the number of matching numbers."""
    matches = 0
    for num in user_nums:
        if num in cpu_nums:
            matches += 1
    return matches

def calculate_winnings(bet: int, matches: int) -> int:
    """Calculates the winnings based on the bet and the number of matches."""
    if matches == 0:
        return 0
    elif 1 <= matches < 4:
        return bet * 1
    elif matches == 4:
        return bet * 2
    elif matches == 5:
        return bet * 3
    elif 6 <= matches < 10:
        return bet * 5
    elif matches == 10:
        return bet * 10
    return 0

def main() -> None:
    """Main function to execute when the script is run directly."""
    print("Welcome to the Kino Machine!")
    bet = int(input("Enter your bet $"))

    while True:
        try:
            nums_to_gen = int(input("How many numbers would you like to generate (5-10): "))
            if 5 <= nums_to_gen <= 10:
                break
            else:
                print("Please enter a number between 5 and 10.")
        except ValueError:
            print("Invalid input. Please enter a valid number between 5 and 10.")

    generated_numbers = number_gen(nums_to_gen)
    print(f"\nThe CPU picked the numbers: {generated_numbers}")

    user_numbers = user_input(nums_to_gen)
    numbers_correct = comparison(generated_numbers, user_numbers)
    winnings = calculate_winnings(bet, numbers_correct)

    print(f"Your numbers: {user_numbers}")
    print(f"You got {numbers_correct} numbers correct!")
    print(f"Your winnings: ${winnings}")
