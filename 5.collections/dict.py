"""
Module Collections - Default Dict

# Review of dictionary
dictionary = {'name': 'marcos', 'age': 33, 'job': 'Software Engineer'}
print(dictionary)
print(dictionary['name'])
print(dictionary['age'])
print(dictionary['job'])
print(dictionary['city']) # KeyError: 'city'
print(dictionary.get('city')) # None
"""

# Default Dict with the creation of a dictionary with a default value, can be used for lambda functions
# That value can use every time that a key is not found in the dictionary
# If we try to access a value that does not exist, this will create a new key with the default value assigned.

from collections import defaultdict

dictionary = defaultdict(lambda: 0)

print(dictionary)

dictionary['name'] = 'marcos'

print(dictionary)

# Evict KeyError and return the default value

print(f'print dictionary -> {dictionary['job']}')
