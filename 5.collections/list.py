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
print(combinedList.sort())
print(combinedList[::1])
print(combinedList[::-1])
print(numbers.reverse())

newListNumber = numbers.copy()
print(newListNumber)

# length of the list
print(len(newListNumber))
