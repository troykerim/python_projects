def harmonic_print(n):
    """Print the harmonic series up to n terms."""
    print("1", end="")
    for i in range(2, n+1):
        print(" + 1/" + str(i), end="")
    print()


def harmonic(n):
    """Compute the nth harmonic number recursively."""
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return 1 / n + harmonic(n-1)


if __name__ == "__main__":
    n = int(input("Enter a value for n: "))

    print("Harmonic series:")
    harmonic_print(n)

    value = harmonic(n)
    print(f"Harmonic value of ({n}) = {value:.3f}")
