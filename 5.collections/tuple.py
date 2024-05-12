"""
Tuple is a collection which is ordered and unchangeable.
Tuple is defined by using comma and not parenthesis.
"""

# Create a tuple - Example 1

listOneTuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(type(listOneTuple))

# Create a tuple - Example 2

listTwoTuple = 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
print(type(listTwoTuple))

tupleSimple = 1
print(type(tupleSimple)) # its a int and not a tuple

tupleSimple = 1,
print(type(tupleSimple)) # its a tuple

tupleSimple = (1)
print(type(tupleSimple)) # its a tuple

# DEFINITIONS - TUPLE
"""
4 -> Its not a tuple
4, -> Its a tuple
(4) -> Its not a tuple
(4,) -> Its a tuple
"""


# Error unpacking tuple

#tupleOne = (1, 2, 3, 4, 5)
#first, second, third = tupleOne

# Definitions Tuple
# Method add and remove not exists in tuple

"""
Tuple sum, max and min only values int or float

For the values of string, you need to use the method len
"""
exampleIntegerOrFloatNumber = (1, 2, 3, 4, 5, 6.0, 7.0)
print(sum(exampleIntegerOrFloatNumber))

print(max(exampleIntegerOrFloatNumber))

print(min(exampleIntegerOrFloatNumber))

# Method Len
exampleIntegerOrFloatNumber = 1, 2, 3, 4, 'a'
print(len(exampleIntegerOrFloatNumber))
