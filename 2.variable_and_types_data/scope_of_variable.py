"""
Scope of variable:
    1. Local variable
    2. Global variable
"""
# 1. Local variable
variable_local = 42
if variable_local > 10:
    novo = variable_local + 10
    #print(novo)

print(novo)

# 2. Global variable
number = 42
#print(number)
#print(type(number))

number = "My balls"
#print(number)
#print(type(number))
