"""
Float type

Float type is a numeric type that can represent real numbers. It is represented by the float class.
"""

# not recommended
value = 1, 44
print(value)
print(type(value))

# recommended
value = 1.44
print(value)
print(type(value))

# possible operations
# tuple operations
value1, value2 = 1, 44
print(value1)
print(type(value1))
print(value2)
print(type(value2))

# convert to number

"""
Observations: Converting an integer to a float results in the loss of the decimal part.
"""
res = int(value)
print(res)


# work with complex number
variable_number_complex = 1 + 2j
print(variable_number_complex)
