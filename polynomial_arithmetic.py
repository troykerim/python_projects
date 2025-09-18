class Polynomial:
    # Initialize the polynomial with a list of coefficients
    def __init__(self, coefficients):
        # Coefficients are ordered from the constant term to the highest degree
        self.coefficients = coefficients

    # Return a string representation of the polynomial for debugging
    def __repr__(self):
        return "Polynomial(" + ", ".join(map(str, self.coefficients)) + ")"

    # Return a human-readable string representation of the polynomial
    def __str__(self):
        # Create a list to hold terms of the polynomial
        terms = []
        # Iterate over the coefficients and their indices
        for i, coef in enumerate(self.coefficients):
            # Skip zero coefficients
            if coef != 0:
                # Add appropriate string for the term based on its degree
                if i == 0:
                    terms.append(str(coef))
                elif i == 1:
                    terms.append(f"{coef}x")
                else:
                    terms.append(f"{coef}x^{i}")
        # Join the terms with ' + ' and return, or return "0" if no terms
        return " + ".join(terms) if terms else "0"

    # Add two polynomials
    def __add__(self, other):
        # Determine the maximum length of the two polynomials
        max_len = max(len(self.coefficients), len(other.coefficients))
        # Initialize the result with zeros
        result = [0] * max_len
        # Add coefficients of the same degree
        for i in range(max_len):
            if i < len(self.coefficients):
                result[i] += self.coefficients[i]
            if i < len(other.coefficients):
                result[i] += other.coefficients[i]
        # Return a new Polynomial object with the result
        return Polynomial(result)

    # Subtract one polynomial from another
    def __sub__(self, other):
        # Determine the maximum length of the two polynomials
        max_len = max(len(self.coefficients), len(other.coefficients))
        # Initialize the result with zeros
        result = [0] * max_len
        # Subtract coefficients of the same degree
        for i in range(max_len):
            if i < len(self.coefficients):
                result[i] += self.coefficients[i]
            if i < len(other.coefficients):
                result[i] -= other.coefficients[i]
        # Return a new Polynomial object with the result
        return Polynomial(result)

    # Multiply two polynomials
    def __mul__(self, other):
        # Initialize the result with zeros, size is sum of lengths minus 1
        result = [0] * (len(self.coefficients) + len(other.coefficients) - 1)
        # Perform polynomial multiplication
        for i, a in enumerate(self.coefficients):
            for j, b in enumerate(other.coefficients):
                result[i + j] += a * b
        # Return a new Polynomial object with the result
        return Polynomial(result)

    # Check if two polynomials are equal
    def __eq__(self, other):
        # Compare coefficients of both polynomials
        return self.coefficients == other.coefficients

    # Differentiate the polynomial
    def differentiate(self):
        # If the polynomial is a constant, return zero polynomial
        if len(self.coefficients) == 1:
            return Polynomial([0])
        # Compute the derivative coefficients
        result = [i * coef for i, coef in enumerate(self.coefficients)][1:]
        # Return a new Polynomial object with the result
        return Polynomial(result)

    # Evaluate the polynomial at a given value of x
    def evaluate(self, x):
        # Compute the polynomial value by summing up the terms
        return sum(coef * (x ** i) for i, coef in enumerate(self.coefficients))


# Example usage:
if __name__ == "__main__":
    # Create polynomial p1: 1 + 2x + 3x^2
    p1 = Polynomial([1, 2, 3])
    # Create polynomial p2: 3 + 4x
    p2 = Polynomial([3, 4])

    # Print polynomial p1
    print("P1:", p1)
    # Print polynomial p2
    print("P2:", p2)

    # Print the result of adding p1 and p2
    print("P1 + P2:", p1 + p2)
    # Print the result of subtracting p2 from p1
    print("P1 - P2:", p1 - p2)
    # Print the result of multiplying p1 and p2
    print("P1 * P2:", p1 * p2)
    # Check and print if p1 and p2 are equal
    print("P1 == P2:", p1 == p2)

    # Print the derivative of p1
    print("P1 differentiated:", p1.differentiate())
    # Print the value of p2 evaluated at x=2
    print("P2 evaluated at x=2:", p2.evaluate(2))
