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

ray = dog(name='Ray', age=2, breed='Poodle')
print(ray)
