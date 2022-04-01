# Recursive function
"""
def factorial(x):
    print(x)
    return x * factorial(x-1)

factorial(5)
"""

def is_even(x):
    if x == 0:
        return True
    else:
        return is_odd(x-1)

def is_odd(x):
    print( not is_even(x))

print(is_odd(2))
#print(is_even(2))

first = {1, 2, 3, 4, 5, 6}
second = {2, 7, 4, 8, 6, 9}

print(first|second)
print(first&second)
print(first-second)
print(first^second)


print([i for i in range(3)])
