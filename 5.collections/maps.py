"""
Maps are a collection of key-value pairs. They are also known as dictionaries in Python.
Dictionary is a collection which is unordered, changeable and indexed. In Python dictionaries are written with curly brackets, and they have keys and values.
"""

receives = {'jan': 100, 'feb': 200, 'mar': 300, 'apr': 400, 'may': 500, 'jun': 600, 'jul': 700, 'aug': 800, 'sep': 900, 'oct': 1000, 'nov': 1100, 'dec': 1200}

# Iterating over a map

# Not recommended way to iterate over a map an Examples 1, 2 and 3

# Example 1 - print keys

for key in receives:
    print(key)

# Example 2 - print values

for key in receives:
    print(receives[key])

# Example 3 - print key-value pairs

for key in receives:
    print(f'In {key} received R$ {receives[key]}')

# Example 4 - Recommended way to iterate over a map
print(receives.keys())

for key in receives.keys():
    print(key)

for key in receives.keys():
    print(receives[key])
