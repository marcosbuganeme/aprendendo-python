"""
List is a collection which is ordered and changeable.
Allows duplicate members.
List in python have dynamic size, so it can grow and shrink as per the requirement.
List in python are mutable, so they can be modified after creation.
"""

type([]) # <class 'list'>

listOfNumbers = [1, 2, 3, 3, 3, 3, 3, 3, 3, 14, 15]
if 15 in listOfNumbers:
    print("Number 15 is in the list")
else:
    print("Number 15 is not in the list")
print(f'Number is 3 = {listOfNumbers.count(3)} x')

listOfCharacters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
if 'k' in listOfCharacters:
    print("Character 'k' is in the list")
else:
    print("Character 'k' is not in the list")

unorderedList = [55, 22, 33, 44, 11, 100, 500, 1, 2, 4, 5]
unorderedList.sort()
print(unorderedList)

listOfMixed = [6, 'k', 5, 'b', 3, 'a', 4, 'l', 8, 'z', 1, 77, 2]

# Separating numbers and strings into different lists
numbers = [item for item in listOfMixed if isinstance(item, int)]

# Sorting each list
numbers.sort()
print(numbers)

# Separating numbers and strings into different lists
strings = [item for item in listOfMixed if isinstance(item, str)]

# Sorting each list
strings.sort()
print(strings)

# Combining the two lists
# Example 1
combinedList = numbers + strings
print(combinedList)

# Example 2
numbers.extend(strings)
print(numbers)

# Sorting each list
print(combinedList[::1])
print(combinedList[::-1])
print(numbers.reverse())

newListNumber = numbers.copy()
print(newListNumber)

# length of the list
print(len(newListNumber))

# Remove element from the list
print(numbers)
elementRemoved = numbers.pop()
print(elementRemoved)
print(numbers)

# Remove element from index the list
print(numbers)
elementRemoved = numbers.pop(2)
print(elementRemoved)
print(numbers)

# Remove all elements of the list
numbers.clear()
print(numbers)

# Duplicating elements of a list
newList = [1, 2, 3, 4, 5]
duplicatedList = newList * 2
print(duplicatedList)

# Split a string into a list
# Example 1
learn = "I am learning Python"
print(learn)
learn = learn.split()
print(learn)

# Example 2
learn = "I,am,learning,Python"
print(learn)
learn = learn.split(',')
print(learn)

# Join a list into a string
# Example 1
learn = ' '.join(learn)
print(learn)

# Example 2
learn = '$'.join(learn)
print(learn)

# Iterating over a list

# Example 1 - Using a for loop
for item in range(len(learn)):
    print(learn[item])

# Example 2 - Using a while loop

carShop = ['BMW', 'Audi', 'Mercedes', 'Toyota', 'Ford', 'Chevrolet', 'Jeep', 'Fiat', 'Honda', 'Hyundai']

productOfCar = ''

while productOfCar != 'quit':
    productOfCar = input('Add a car to the list or type "quit" to exit:')
    if productOfCar != 'quit':
        carShop.append(productOfCar)

for car in carShop:
    print(car)


# Index of an element in a list
colors = ['green', 'blue', 'red', 'yellow', 'black', 'white', 'purple', 'orange', 'pink', 'brown']

# Example 1
print(colors[2]) # red

# Example 2
print(colors.index('red')) # return '2' as the index of the element 'red'

# Example 3
print(colors[-3]) # orange

# Generating index and value of a list
for index, value in enumerate(colors):
    print(index, value)

# List accepts values repeated and any data type
newList = []
newList.append(1)
newList.append(1)
newList.append(1)
newList.append(2)
newList.append(3)
newList.append(5)
print(newList)

# Indexing not found
# newList[10] # IndexError: list index out of range
#print(newList[10])

# Search index of a value
print(newList.index(5, 5)) # 5

# Search index at range of values
print(newList.index(5, 0, 6)) # 5


"""
Working with slices
list[start:stop:step]
range(start, stop, step)
"""

# Example 1 - list start

newList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(newList[1:])

# Example 2 - list end
print(newList[:5])

# Example 3 - list start and end
print(newList[1:5])

# Example 4 - list start and step
print(newList[1::2])
