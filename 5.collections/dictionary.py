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

# Remove an element from dictionary

# Example 1 - Recovery the value of element removed
invoices.pop('water')

print(invoices)

# Example 2 - Remove an element without recovery the value
del invoices['gas']

print(invoices)

"""
Use cases in the real world apply dictionary in Python

Dictionaries in Python are extremely versatile and useful in many programming scenarios. Here are some common use cases for using dictionaries:

1. Storing Configuration Data: Dictionaries are ideal for storing application settings or user preferences due to their key-value structure, making it easy to retrieve and modify specific settings.

2. Implementing a Cache: Using dictionaries to store the results of computationally expensive operations allows previous results to be quickly retrieved using keys, reducing the need to repeat calculations.

3. Frequency Counting: Dictionaries are useful for counting the frequency of items in a collection, such as counting the number of times each word appears in a text.

4. Mapping Relationships Between Data: Dictionaries can be used to map relationships between different types of data, such as associating user IDs with their information or products with their prices.

5. Modeling Objects or Structures: In some cases, it may be practical to model objects or complex structures as dictionaries, especially when the data are dynamic and the structure can vary.

6. Grouping Functions or Operations: A dictionary can store functions as values, allowing dynamic access to different operations or commands based on a key.

7. Unpacking Data into Functions: Dictionaries can be used to unpack data directly into function arguments using the unpacking operator (**), which is particularly useful in functions that require a large number of named parameters.
"""

# Use the list
carShop = []

product1 = ['Playstation 5', 5000, 'Sony']
product2 = ['Xbox Series X', 4500, 'Microsoft']

carShop.append(product1)
carShop.append(product2)

print(carShop)

# Use the tuple
carShop = []

product1 = ('Playstation 5', 5000, 'Sony')
product2 = ('Xbox Series X', 4500, 'Microsoft')

carShop = (product1, product2)

print(carShop)

# Use the dictionary
carShop = []

product1 = {'name': 'Playstation 5', 'price': 5000, 'brand': 'Sony'}
product2 = {'name': 'Xbox Series X', 'price': 4500, 'brand': 'Microsoft'}

carShop.append(product1)
carShop.append(product2)

print(carShop)


# Methods in dictionary

# clear() - Removes all the elements from the dictionary

# Example

carShop.clear()
print(carShop)

# Copy() - Returns a copy of the dictionary

revenues = {
    'January': 1000,
    'February': 2000,
    'March': 3000
}

print(revenues)

# Example 1 - Deep Copy

oldRevenue = revenues.copy()

print(oldRevenue)

revenues['April'] = 4000

print(revenues)
print(oldRevenue)

# Example 2 - Shallow Copy

newRevenue = revenues
print(newRevenue)

newRevenue['May'] = 5000
print(revenues)
print(newRevenue)


# Form not usual to create a dictionary
# Example 1
other = {}.fromkeys('a', 'b')

print(other)
print(type(other))
