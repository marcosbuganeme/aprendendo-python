"""
Boolean type

Boolean type is a data type that can only represent two values: True and False. It is represented by the bool class.

# not recommended
true, false

# correct
True, False
"""
active = False

"""
Operations with boolean type
"""
# Negation (not)
print("Operation Not")
print(not active)

# Or
"""
The operator or returns True if at least one of the operands is True.
"""

logged = True
print("Operation Or")
print(active or logged)

# And
"""
The operator and returns True if both operands are True.
"""
print("Operation And")
print(active and logged)
