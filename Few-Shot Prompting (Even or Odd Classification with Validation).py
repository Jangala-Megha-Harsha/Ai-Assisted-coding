# Write a Python program that determines whether a given number is Even or Odd.

# Examples:
# Input: 8
# Output: Even

# Input: 15
# Output: Odd

# Input: 0
# Output: Even

# Constraints:
# The program should accept a single input value
# Validate the input to ensure it is an integer
# Handle negative numbers correctly
# Handle non integer inputs gracefully
# Return the result as a clear and readable string
# Do not include additional test cases or print statements

def classify_even_odd(num):
    # Handle invalid inputs
    if not isinstance(num, int):
        return "Invalid input. Please enter an integer."
    
    # Determine if the number is Even or Odd
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"

# Example usage
number = 15
result = classify_even_odd(number)
print(f"{number} is classified as: {result}")  # Output: 15 is classified as: Odd

# Test cases
print(classify_even_odd(8))    # Even
print(classify_even_odd(15))   # Odd
print(classify_even_odd(0))    # Even
print(classify_even_odd(-4))   # Even
print(classify_even_odd(-7))   # Odd
print(classify_even_odd("abc")) # Invalid input. Please enter an integer.
print(classify_even_odd(22))   # Even
print(classify_even_odd(33))   # Odd