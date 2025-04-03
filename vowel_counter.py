# Vowel counter

vowels = ['a', 'e', 'i', 'o', 'u']
count = 0 
sen = ""
print("Enter a sentence below and let's count the number of vowels")
sen = input("Enter here: ").lower()
str_len = len(sen)

for char in sen:
    if char in vowels:
        count += 1 

print("\n")
print("Here is the original sentence: ", sen)
print("\n")
print("Your sentence had", count, "number of vowels")