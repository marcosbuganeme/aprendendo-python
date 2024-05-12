"""
While loops are used to execute a block of code multiple times as long as a condition is true.
"""

count = 1
while count <= 5:
    print(count)
    count += 1

number = 0
while number != 42:
    number = int(input("Input a number (42) to stop:"))

while True:
    user_input = input("Input 'quit' to stop:")
    if user_input == "quit":
        break
    print("Você digitou:", user_input)

soma = 0
while True:
    num = int(input("Input a number (0 to stop):"))
    if num == 0:
        break
    soma += num
print("A soma total é:", soma)


n = 2
while n <= 10:
    print(n)
    n += 2
