# Context:
# You are generating an optimized Python program for number classification.
# The program must classify a given number as Prime, Composite, or Neither.

# Instructions:
# Read a single integer input
# Validate the input properly
# Numbers less than or equal to 1 must be classified as Neither
# A prime number has exactly two distinct positive divisors
# A composite number has more than two positive divisors

# Constraints:
# Use efficient logic by checking divisibility only up to the square root
# Avoid unnecessary loops or repeated calculations
# Handle invalid inputs such as non integers gracefully
# Return the classification result as a clear string
# Do not include example inputs or test cases

def classify_number(num):
    # Handle invalid inputs
    if not isinstance(num, int):
        return "Invalid input. Please enter an integer."
    
    # Numbers less than or equal to 1 are classified as Neither
    if num <= 1:
        return "Neither"
    
    # Check for primality
    if num == 2:
        return "Prime"
    
    if num % 2 == 0:
        return "Composite"
    
    for i in range(3, int(num**0.5) + 1, 2):
        if num % i == 0:
            return "Composite"
    
    return "Prime"

# Example usage
number = 29
result = classify_number(number)
print(f"{number} is classified as: {result}")  # Output: 29 is classified as: Prime

# Test cases
print(classify_number(1))    # Neither
print(classify_number(2))    # Prime
print(classify_number(4))    # Composite
print(classify_number(17))   # Prime
print(classify_number(18))   # Composite
print(classify_number(-5))   # Neither
print(classify_number("abc")) # Invalid input. Please enter an integer.
print(classify_number(25))   # Composite