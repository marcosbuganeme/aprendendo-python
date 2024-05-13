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

# Iterating over a set

for i in my_set:
    print(i)


#  Remove duplicate elements from a list
cities = {'São Paulo', 'São Paulo', 'São Paulo', 'Rio de Janeiro', 'Rio de Janeiro', 'Rio de Janeiro', 'Goiânia', 'Floripa'}

print(cities)
print(len(cities))

# Remove an element explicit at set

# Example 1
cities.remove('São Paulo')
print(cities)
print(len(cities))

# Example 2
cities.discard('Rio de Janeiro')
print(cities)
print(len(cities))

# Observation: If the element does not exist in the set, the remove() method will raise an error, while the discard() method will not.

# Copying a set to another set
oddSet = {1, 3, 5}
print(oddSet)


# Example 1 - Deep Copy

newOddSet = oddSet.copy()

newOddSet.add(7)

print(oddSet)
print(newOddSet)

# Example 2 - Shallow Copy

newOddSet = oddSet

newOddSet.add(7)

print(oddSet)
print(newOddSet)

# Remove all elements from a set

oddSet.clear()
print(oddSet)

newOddSet.clear()
print(newOddSet)

# Method mathematics in set

studentsPython = {'Marcos', 'Patricia', 'Ellen', 'Pedro', 'Julia'}
studentsJava = {'Marcos', 'Fernando', 'Gustavo', 'Julia', 'Ellen'}

# Observation we can use the method union() or the operator | to join the sets
# All students from Python and Java courses

# Example 1 - Union

unionExample1 = studentsPython.union(studentsJava) # output {'Julia', 'Gustavo', 'Fernando', 'Pedro', 'Patricia', 'Marcos', 'Ellen'}
print(f'example 1 - all students in both courses {unionExample1}')

# Example 2 - Pipe

unionExample2 = studentsPython | studentsJava # output {'Julia', 'Gustavo', 'Fernando', 'Pedro', 'Patricia', 'Marcos', 'Ellen'}
print(f'example 2 - all students in both courses {unionExample2}')

# Generate a set of students who are in both courses

# Example 1 - Intersection

intersectionExample1 = studentsPython.intersection(studentsJava) # output {'Julia', 'Marcos', 'Ellen'}
print(f'example 1 - student in both courses: {intersectionExample1}')

# Example 2 - Intersection

intersectionExample2 = studentsPython & studentsJava # output {'Julia', 'Marcos', 'Ellen'}
print(f'example 2 - student in both courses: {intersectionExample2}')


# Generate a set of students who are only in one course

# Print students who are only in Python course
studentOnlyPython = studentsPython.difference(studentsJava) # output {'Pedro', 'Patricia'}
print(f'student only python: {studentOnlyPython}')

# Print students who are only in Java course
studentOnlyJava = studentsJava.difference(studentsPython) # output {'Gustavo', 'Fernando'}
print(f'student only java: {studentOnlyJava}')

"""
Operations with sets

1. sum() - Sum values
2. max() - Maximum value
3. min() - Minimum value
4. len() - Number of elements
"""

newHashSet = {1, 2, 3, 4, 5, 6}

# Operation Sum
print(sum(newHashSet))


