"""
Receive data from user
"""

# input data from user
name = input("What's your name?")
print("Nice to meet you,", name)

age = int(input("How old are you?"))
print("You are", age, "years old.")

# process data
print("You were born in ", 2024 - int(age))

# output data
# example print 2.x
print('%s years old %s' % (age, name))

# example print 3.4 or less
print('{0} years old {1}'.format(age, name))

# example print 3.6+
print(f'{name} years old {age}')
