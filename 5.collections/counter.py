"""
Module Collections - Counter

Counter -> High-performance container datatypes

Counter is a subclass of dictionary class. It is used to keep the count of the elements in an iterable in the form of an unordered collection of elements. It is an unordered collection where elements are stored as dictionary keys and their counts are stored as dictionary values.

Collections in Python are containers that are used to store collections of data, for example, list, dict, set, tuple etc. These are built-in collections. Several modules have been developed that provide additional data structures to store collections of data. One such module is the Python Counter module.
"""

# Use of Counter

from collections import Counter

listOfNumbers = [1, 2, 3, 4, 1, 2, 3, 1, 2, 1, 34, 35, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(f'List of numbers: {listOfNumbers}')

# Print result
result = Counter(listOfNumbers)

print(result)
print(type(result)) # Counter({1: 6, 2: 5, 3: 4, 4: 3, 5: 2, 6: 2, 7: 2, 8: 2, 9: 2, 0: 2, 34: 1, 35: 1})

"""
Observation of Counter result
1. The result is a dictionary with the elements of the list as keys and their counts as values.
2. The elements are stored as dictionary keys and their counts are stored as dictionary values.
"""


# Example 2 - Count the frequency of words in a string
# Count the frequency of words in a string

string = 'Python is a high-level programming language. Python is a high-level programming language. Python is a high-level programming language.'

result = Counter(string)
print(result)

# Example 3 - Count the frequency of words in a list

textRandom = """Collections in Python are containers that are used to store collections of data, for example, list, dict, set, tuple etc. These are built-in collections. Several modules have been developed that provide additional data structures to store collections of data. One such module is the Python Counter module."""

words = textRandom.split()

# Print result
result = Counter(words)
print(result)

# Search a five words most common

statistics = result.most_common(5)
print(statistics)
