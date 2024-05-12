"""
Dictionary in python is an unordered collection of data in a key:value pair form.

Dictionary is a collection which is unordered, changeable and indexed. In Python dictionaries are written with curly brackets, and they have keys and values.

Dictionary items are presented in key:value pairs, and can be referred to by using the key name.

Keys are unique within a dictionary while values may not be. The values of a dictionary can be of any type, but the keys must be of an immutable data type such as strings, numbers, or tuples.

print(type({}))

"""

print(type({}))

# Creating a dictionary - Example 1

countries = {
    'BR': 'Brazil',
    'US': 'United States',
    'JP': 'Japan',
    'DE': 'Germany',
    'IT': 'Italy',
    'FR': 'France',
    'UK': 'United Kingdom',
    'CN': 'China',
    'IN': 'India',
    'RU': 'Russia'
}

print(countries)

print(type(countries))


# Creating a dictionary - Example 2

countries = dict(BR='Brazil', US='United States', JP='Japan', DE='Germany', IT='Italy', FR='France', UK='United Kingdom', CN='China', IN='India', RU='Russia')

print(countries)


# Accessing a element in dictionary

print(countries['BR'])
