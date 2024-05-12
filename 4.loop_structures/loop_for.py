"""
Use Loop For with iterable objects such as lists, tuples, strings, dictionaries, etc.
"""

oddNumbers: list[int] = [1, 3, 5, 7, 9]
print(oddNumbers)

for odd in oddNumbers:
    print(odd)

rangeOfNumbers: range = range(1, 10)
print(rangeOfNumbers)

for number in rangeOfNumbers:
    print(number)


phrase: str = "Python is a programming language"
print(phrase)

for letter in phrase:
    print(letter)

for i, v in enumerate(phrase):
    print(i, v)

# Omitting the index
for _, v in enumerate(phrase):
    print(v)

quantity: int = int(input("Enter the quantity of loops: "))
sum = 0

for n in range(1, quantity + 1):
    number = int(input(f"Enter the number {n}: "))
    sum += number
print(sum)

"""
Table of Emojis
https://apps.timwhitlock.info/emoji/tables/unicode
"""

for _ in range(3):
    for num in range(1, 11):
        print("\U0001F600" * num)
