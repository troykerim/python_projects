def mod(a):
    results = {}
    for i in range(1, a+1):
        results[i] = a % i == 0
    return results

print("Remainder checker")
a = int(input("Enter a number: "))
b = mod(a)
print(f"Modulus results for {a}: ")
for divisor, is_divisable in b.items():
    print(f"{a} % {divisor} = 0 {is_divisable}")