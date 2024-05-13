"""
Module Collections - Named Tuple

Named tuple is a tuple with named fields. It is a subclass of the tuple class.
"""

# Review Tuple

my_tuple = (1, 2, 3)
print(my_tuple[0])


# Use Named Tuple

from collections import namedtuple

# Define a named tuple

# Creation of a named tuple

# Example 1
dog = namedtuple('dog', 'name age breed')
print(dog)


# Example 2
dog = namedtuple('dog', 'name, age, breed')
print(dog)


# Example 3
dog = namedtuple('dog', ['name', 'age', 'breed'])
print(dog)


# Use a named tuple

jo = dog(name='jo', age=9, breed='street dog')
print(jo)

# Access the fields of the named tuple

print(jo[0])
print(jo[1])
print(jo[2])

# Other ways to create a named tuple
print(jo.name)
print(jo.age)
print(jo.breed)
