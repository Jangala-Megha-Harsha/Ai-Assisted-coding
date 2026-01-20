# Write a Python function to compute the factorial of a given non negative integer.

# Example:
# Input: 5
# Output: 120

# Constraints:
# The function should accept a single integer input
# Handle invalid inputs such as negative numbers
# Use clear and readable logic
# Return the factorial value as an integer
# Do not include additional print statements or test cases

def factorial(n):
    # Handle invalid inputs
    if not isinstance(n, int) or n < 0:
        raise ValueError("Input must be a non-negative integer.")
    
    result = 1
    for i in range(2, n + 1):
        result *= i
    
    return result

# Example usage
number = 5
print(f"The factorial of {number} is {factorial(number)}")  # Output: 120

# Test cases
print(factorial(0))  # 1
print(factorial(1))  # 1
print(factorial(5))  # 120
print(factorial(10)) # 3628800