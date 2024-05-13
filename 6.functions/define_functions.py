"""
Define Functions

1. Functions are a block of code that performs a specific task. 2. Functions are reusable code blocks that can be called multiple times in a program.
3. Functions are defined using the 'def' keyword followed by the function name and parentheses.
4. The function body is indented.
"""

# Example 1: Define a function
def greet():
    print("Hello, World!")

# Call the function
greet()


# Example 2 - Define a function with parameters
def greet(name):
    print(f"Hello, {name}!")

# Call the function
greet('Marcos')


# Example 3 - Define a function with a return value
def sum_two_numbers(a, b):
    return a + b

# Call the function
result = sum_two_numbers(5, 3)
print(result)

# DRY Principle
# Don't Repeat Yourself
# Reuse code by defining functions

# Example 4 - Define a function with default arguments
def greet(name='World !!'):
    print(f"Hello, {name}!")

# Call the function
greet()
