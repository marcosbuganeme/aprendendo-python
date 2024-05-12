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

# Concatenation tuple

tupleOne = (1, 2, 3, 4, 5)
print(tupleOne)

tupleTwo = (6, 7, 8, 9, 10)
print(tupleTwo)

print(tupleOne + tupleTwo)

# Verify if a value exists in tuple

print(1 in tupleOne)

# Iterate over a tuple

for number in tupleOne:
    print(number)

for index, number in enumerate(tupleOne):
    print(index, number)

# Count the number of occurrences of a value in a tuple

print(tupleOne.count(1))

# Utilize tuple every time that you need to create a collection that you don't need to change the values

months = ('January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December')

print(months)

# Accessing index of a tuple

print(months.index('January'))
print(months[0])

# If element not exists in tuple, the method index return a error
"""
print(months.index('Saturday')) # ValieError: tuple.index(x): x not in tuple

print(months[20]) # ValueError: tuple.index(x): x not in tuple
"""

# Slicing tuple example
# tuple[start:stop:step]
print(months[0:12:2])

"""
Whats the difference between tuple and list?
1. Tuples are faster than lists.
2. Tuples are immutable.
3. Tuples secure data integrity.
4. Tuples are used as keys in dictionaries.
"""

# Copying a tuple
oldTuple = (1, 2, 3, 4, 5)
print(oldTuple)

newTuple = oldTuple

# In tuples not problem shallow copy

print(newTuple)
print(oldTuple)

otherTuple = (6, 7, 8, 9, 10)
print(otherTuple)

newTuple = newTuple + otherTuple

print(newTuple)
print(otherTuple)
