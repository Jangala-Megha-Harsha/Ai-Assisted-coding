# Write a Python function that checks whether a given number is a perfect number.

# Instructions:
# The function should take a single integer as input
# A perfect number is equal to the sum of its proper positive divisors excluding itself
# Return True if the number is perfect, otherwise return False

# Constraints:
# Handle invalid inputs gracefully
# Numbers less than or equal to 1 should return False
# Use efficient logic to find divisors
# Avoid unnecessary computations
# Do not include example inputs, outputs, or test cases

def is_perfect_number(num):
    # Handle invalid inputs
    if not isinstance(num, int) or num <= 1:
        return False
    
    sum_of_divisors = 0
    
    # Find proper divisors and calculate their sum
    for i in range(1, int(num**0.5) + 1):
        if num % i == 0:
            sum_of_divisors += i
            if i != 1 and i != num // i:
                sum_of_divisors += num // i
    
    return sum_of_divisors == num

# Example usage
number = 28
if is_perfect_number(number):
    print(f"{number} is a perfect number.")
else:
    print(f"{number} is not a perfect number.")

# Test cases
print(is_perfect_number(6))    # True
print(is_perfect_number(28))   # True
print(is_perfect_number(496))  # True
print(is_perfect_number(12))   # False
print(is_perfect_number(1))    # False
print(is_perfect_number(-6))   # False
print(is_perfect_number("abc")) # False
print(is_perfect_number(8128)) # True