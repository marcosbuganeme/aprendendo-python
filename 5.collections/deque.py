"""
Module Collections - Deque

We can use the deque class to create a double-ended queue. It is a subclass of the list.

High-performance container datatypes
"""

from collections import deque

# Create a deque int

my_deque = deque([1, 2, 3, 4, 5])
print(my_deque)

# Create a deque string

my_deque = deque('python')
print(my_deque)

# Add elements to the right
my_deque.append('i')
print(my_deque)


# Add elements to the left
my_deque.appendleft('h')
print(my_deque)


# Remove elements from the right
my_deque.pop()
print(my_deque)

# Remove elements from the left
my_deque.popleft()
print(my_deque)
