"""
Set is a collection of unique elements.
Characteristics of Set are:
1. Set is mutable.
2. Set is unordered.
3. Set is not indexed.
4. Set is iterable.
5. Set is not hashable.

Different ways to create a set:
1. Using set() constructor.
2. Using curly braces {}.
3. Using set comprehension.
4. Using set() constructor with iterable object.
5. Using set() constructor with dictionary.
6. Using set() constructor with string.
7. Using set() constructor with tuple.
8. Using set() constructor with list.
9. Using set() constructor with range().
10. Using set() constructor with map().
11. Using set() constructor with filter().
12. Using set() constructor with zip().
13. Using set() constructor with enumerate().
14. Using set() constructor with dictionary comprehension.
"""

# Defining a set

# Example 1: Using set() constructor
my_set = set()
print(my_set)  # Output: set()
print(type(my_set))  # Output: <class 'set'>

my_set = set([1, 2, 3, 4, 5, 5, 4, 3, 2, 1, 10, 9, 8, 7, 6])
print(my_set)  # Output: {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

# Example 2: Using curly braces {}
my_set = {1, 2, 3, 4, 5, 5, 4, 3, 2, 1, 10, 9, 8, 7, 6}
print(my_set)  # Output: {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
print(type(my_set))  # Output: <class 'set'>

my_set = set(range(1, 11))
print(my_set)  # Output: {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
print(type(my_set))  # Output: <class 'set'>
