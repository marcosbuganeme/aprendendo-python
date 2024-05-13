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
print(countries.get('BR'))

# Accessing a element not exists in dictionary
#print(countries['XL']) # KeyError: 'XL'

print(countries.get('XL'))

brazil = countries.get('BR')

if brazil:
    print('Country found')
else:
    print('Country not found')

# Dictionary accepts value default
print(countries.get('XL', 'Country not found'))

# Return True or False if key exists in dictionary
print('BR' in countries)

# Iterating over dictionary
# Example 1

for key in countries:
    print(key, countries[key])

# Example 2

for key, value in countries.items():
    print(key, value)

# Print only keys

for key in countries.keys():
    print(key)

# Print only value

for value in countries.values():
    print(value)

# We can use any data types (int, float, string, boolean, lists, tuples) as key in dictionaries.

# Example 1 - Tuple as key in dictionary

localities = {
    (35.6895, 139.6917): 'Tokyo',
    (40.7128, 74.0060): 'New York',
    (48.8566, 2.3522): 'Paris',
    (51.5074, 0.1278): 'London',
    (55.7558, 37.6176): 'Moscow'
}

print(localities)
print(type(localities))

# Adding a new element in dictionary
# Example create a new dictionary with empty dictionary and add elements
recipes = {
    'Pasta': 'Italian',
    'Sushi': 'Japanese',
    'Tacos': 'Mexican'
}

print(recipes)

# Example 1

recipes['Insects'] = 'Chinese'

print(recipes)


# Example 2

recipes.update({'Burger': 'American'})

print(recipes)

# Update a value in dictionary
# Example 1

invoices = {
    'water': 100,
    'gas': 200,
    'tax': 300
}

print(invoices)

invoices.update({'water': 150})

print(invoices)

"""
Conclusion
In dictionary, we can store any data types as key and value.

Dictionary is mutable, we can add, update and delete elements in dictionary.

Dictionary is unordered collection of data in key:value pair form.

1. We can iterate over dictionary using for loop.
2. We can use in operator to check if key exists in dictionary.
3. We can use get method to get value of key in dictionary.
4. We can use keys method to get all keys in dictionary.
5. We can use values method to get all values in dictionary.
6. The dictionary key is unique.
"""
