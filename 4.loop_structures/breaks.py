"""
Functions to demonstrate the use of break statements in loops.
Quite useful for when you need to stop a loop before it reaches the end.
With work equal java or c.
"""

# Example 1

for number in range(1, 10):
    if number == 5:
        break
    else:
        print(number)
    print("Loop ended.")

# Example 2

while True:
    user_input = input("Input 'quit' to stop:")
    if user_input == "quit":
        break
    print("Your digit: ", user_input)
