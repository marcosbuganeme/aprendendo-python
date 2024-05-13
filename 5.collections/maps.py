"""
Maps are a collection of key-value pairs. They are also known as dictionaries in Python.
Dictionary is a collection which is unordered, changeable and indexed. In Python dictionaries are written with curly brackets, and they have keys and values.
"""

receives = {'jan': 100, 'feb': 200, 'mar': 300, 'apr': 400, 'may': 500, 'jun': 600, 'jul': 700, 'aug': 800, 'sep': 900, 'oct': 1000, 'nov': 1100, 'dec': 1200}

# Iterating over a map

# Example 1

for key in receives:
    print(key)

# Example 2

for key in receives:
    print(receives[key])
