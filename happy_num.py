def is_happy_num(n):
    past = set() # Store previous encountered numbers 
    while n != 1:
        n = sum(int(i) ** 2 for i in str(n))
        if n in past:
            return False 
        past.add(n)
    return True

def gen_happy_numbers(count):
    happy_nums = []
    num = 1
    while len(happy_nums) < count:
        if is_happy_num(num):
            happy_nums.append(num)
        num += 1 
    return happy_nums
    
print("Happy numbers program.")        
n = int(input("Enter how many happy numbers you want: "))
happy_nums = gen_happy_numbers(n)

print(f"Here are {n} happy numbers: {happy_nums}")