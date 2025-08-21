def harmonic(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return 1 / n + harmonic(n-1) 

print(harmonic(7))
print(harmonic(2))
print(harmonic(10))