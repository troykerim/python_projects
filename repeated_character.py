# Repeat the character 

print("Character repeater")
letter = input("Enter a character: ")
repeat = int(input("How many times do you wnat it repeated: "))

for i in range(repeat):
    if letter.isupper():
        print(letter.upper(), end="")
    else:
        print(letter, end="")
