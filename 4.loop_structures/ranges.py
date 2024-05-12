"""
Learn loops with ranges.
Learn how to use the range function to generate a sequence of numbers.
Ranges are used to generate a sequence of numbers.
"""

print('------------------')
# Form 1: range(stop)
print('FORM 1')
for num in range(10):
    print(num)


print('------------------')
# Form 2: range(start, stop)
print('FORM 2')
for num in range(1, 10):
    print(num)

print('------------------')
# Form 3: range(start, stop, step)
print('FORM 3')
for num in range(1, 10, 2):
    print(num)

print('------------------')
# Form 4: range(stop, start, step)
print('FORM 4')
for num in range(10, 1, -2):
    print(num)

"""
Table of Emojis
https://apps.timwhitlock.info/emoji/tables/unicode
"""

print('------------------')
# Using range to print emojis
for num in range(128000, 128514):
    #print(chr(num), end=' ')
    break

print('------------------')
for num in range(1, 10, 1):
    print('\U0001F600' * num)

#count = 0
for num in range(10, 0, -1):
    #count += 1
    print('\U0001F600' * num)
