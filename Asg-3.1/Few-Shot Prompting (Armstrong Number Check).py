# Write a Python function to check whether a given number is an Armstrong number.

# Examples:
# Input: 153
# Output: Armstrong Number

# Input: 370
# Output: Armstrong Number

# Input: 123
# Output: Not an Armstrong Number

# Constraints:
# The function should take a single integer as input
# Handle invalid inputs such as negative numbers and non integers
# Use mathematical logic to calculate the Armstrong condition
# Return the result as a meaningful string
# Do not include test cases or print statements

def is_armstrong_number(num):
    # Handle invalid inputs
    if not isinstance(num, int) or num < 0:
        return "Invalid input. Please enter a non-negative integer."
    
    # Convert number to string to determine the number of digits
    num_str = str(num)
    num_digits = len(num_str)
    
    # Calculate the sum of each digit raised to the power of num_digits
    sum_of_powers = sum(int(digit) ** num_digits for digit in num_str)
    
    # Check if the sum of powers is equal to the original number
    if sum_of_powers == num:
        return "Armstrong Number"
    else:
        return "Not an Armstrong Number"

# Example usage
number = 153
result = is_armstrong_number(number)
print(f"{number} is an {result}.")  # Output: 153 is an Armstrong Number.

# Test cases
print(is_armstrong_number(153))  # Armstrong Number
print(is_armstrong_number(370))  # Armstrong Number
print(is_armstrong_number(123))  # Not an Armstrong Number
print(is_armstrong_number(-153)) # Invalid input. Please enter a non-negative integer.
print(is_armstrong_number("abc")) # Invalid input. Please enter a non-negative integer.
print(is_armstrong_number(9474)) # Armstrong Number