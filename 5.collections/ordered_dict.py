"""
Module Collections - Ordered Dict
"""

dictionary = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
print(dictionary)

# The order of the elements is not guaranteed
for key, value in dictionary.items():
    print(f'key={key}, value={value}')
