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

# Condition: Set cannot have mutable elements like list, set, dictionary.

# Example 3: Using set comprehension
my_set = {x for x in range(1, 11)}
print(my_set)  # Output: {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

# Comparing list, tuples, dictionaries and sets

# Lists accepted values repeated
list1 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(f'List: {list1} is quantity elements: {len(list1)}')

# Tuples accepted values repeated
tuple1 = (10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(f'Tuple: {tuple1} is quantity elements: {len(tuple1)}')

# Dictionaries is not accepted values repeated
dict1 = {}.fromkeys([10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 'default')
print(f'Dictionary: {dict1} is quantity elements: {len(dict1)}')

# Sets is not accepted values repeated
set1 = {10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
print(f'Set: {set1} is quantity elements: {len(set1)}')

# Types of data that can be used in a set (int, float, string, tuple, range, map, filter, zip, enumerate)

my_set = {10, 9.5, 'Python', (1, 2, 3), range(1, 11), map(lambda x: x, range(1, 11))}
print(my_set)
print(type(my_set))
