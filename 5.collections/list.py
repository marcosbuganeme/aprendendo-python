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
