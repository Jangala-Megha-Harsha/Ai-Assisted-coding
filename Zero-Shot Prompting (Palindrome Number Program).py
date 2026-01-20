# Write an optimized Python program to check whether a given number is a palindrome.

# Constraints:
# Handle invalid inputs gracefully
# Use efficient logic without converting the number to a string
# Negative numbers should return False
# Single digit numbers should return True
# The function should return a boolean value

def is_palindrome_number(num):
    # Handle invalid inputs
    if not isinstance(num, int):
        return False
    # Negative numbers are not palindromes
    if num < 0:
        return False
    # Single digit numbers are palindromes
    if num < 10:
        return True
    
    original_num = num
    reversed_num = 0
    
    while num > 0:
        digit = num % 10
        reversed_num = reversed_num * 10 + digit
        num //= 10
    
    return original_num == reversed_num

# Test cases
print(is_palindrome_number(121))  # True
print(is_palindrome_number(-121)) # False
print(is_palindrome_number(10))   # False
print(is_palindrome_number(12321)) # True
print(is_palindrome_number(5))    # True
print(is_palindrome_number("abc")) # False
# Example usage
number = 12321
if is_palindrome_number(number):
    print(f"{number} is a palindrome.")
else:
    print(f"{number} is not a palindrome.")