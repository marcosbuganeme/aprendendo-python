"""
Module Collections - Ordered Dict
"""

dictionary = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
print(dictionary)

# The order of the elements is not guaranteed
for key, value in dictionary.items():
    print(f'key={key}, value={value}')


from collections import OrderedDict

# Ordered Dict maintains the order of the elements
# Ensure the order of insertion of elements

ordered_dictionary = OrderedDict({'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5})
print(ordered_dictionary)

for key, value in ordered_dictionary.items():
    print(f'key={key}, value={value}')


# Difference between Dict and Ordered Dict

# Dict

dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 2, 'a': 1}

# Order the elements in the dictionary does not matter
print(dict1 == dict2) # True


# Ordered Dict

dict1 = OrderedDict({'a': 1, 'b': 2})
dict2 = OrderedDict({'b': 2, 'a': 1})

print(dict1 == dict2) # False
# Order of the elements in the dictionary matters
