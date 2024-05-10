"""
Structure of the logical operators [and, or, not and is]

Operators are used to perform operations on variables and values.

Operator unary: not, is

Operator binary: and, or
"""

active = True
logged = True

# Using the 'and' operator

if active and logged:
    print("Welcome to the system")
else:
    print("You are not allowed to enter the system")

# Using the 'or' operator

logged = False

if active or logged:
    print("Welcome to the system")
else:
    print("You are not allowed to enter the system")

# Using the 'not' operator

if not active:
    print("You are not allowed to enter the system")
else:
    print("Welcome to the system")

# Using the 'is' operator
active = False

if active is False:
    print("You are not allowed to enter the system")

