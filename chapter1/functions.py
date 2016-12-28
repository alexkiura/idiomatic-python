"""Idiomatic ways of writing functions."""

# Scenario 1: using a mutable object as default value for a function argument
# harmful
def f(a, L=[]):
    L.append(a)
    return L

print(f(1))
print(f(2))
print(f(3))

# output is:
# [1]
# [1, 2]
# [1, 2, 3]

# Idiomatic
def f(a, L=[]):
    if L is None:
        L = []
    L.append(a)
    return L

print(f(1))
print(f(2))
print(f(3))

# output is:
# [1]
# [2]
# [3]

# Scenario 2: using return to evaluate expressions in additon to return values
# harmful
def all_equal(a, b, c):
    result = False
    if a == b == c:
        result = True
    return result

# Idiomatic
def all_equal(a, b, c):
    return a == b == c

# Scenario 3: using keyword args for optional arguments.
# harmful
def print_list(list_value, sep):
    print('{}'.format(sep).join(list_value))

the_list = ['a', 'b', 'c']
the_other_list = ['Jeff', 'Hates', 'Java']
print_list(the_list, '')
print_list(the_other_list, ' ')
print_list(the_other_list, ', ')

# Idiomatic
def print_list(list_value, sep=' '):
    print('{}'.format(sep).join(list_value))

the_list = ['a', 'b', 'c']
the_other_list = ['Jeff', 'Hates', 'Java']
print_list(the_list)
print_list(the_other_list)
print_list(the_other_list, ', ')

# Scenario 4: using *args and *kwargs to accept arbitrary arguments
# harmful
def wrap_add_for_console_output(x, y):
    print('-----------------------')
    print(str(x + y))
    print('-----------------------')

wrap_add_for_console_output(2, 3)

# Idiomatic
def for_console_output(func):
    def wrapper(*args, **kwargs):
        print('-----------------------')
        print(str(func(*args, **kwargs)))
        print('-----------------------')
    return wrapper

@for_console_output
def add(x, y):
    return x + y

add(3, 2)

# Scenario 5: treating functions as values
# harmful
def print_addition_table():
    for x in range(0,5):
        for y in range(0, 5):
            if x <= 4:
                print(x + y, end=' ')
            else:
                print('')
def print_subtraction_table():
    for x in range(0,5):
        for y in range(0, 5):
            if x >= 1:
                print(x - y, end=' ')
            else:
                print('')
def print_multiplication_table():
    for x in range(0,5):
        for y in range(0, 5):
            if x <= 4:
                print(x * y, end=' ')
            else:
                print('')
def print_division_table():
    for x in range(0,5):
        for y in range(0, 5):
            if x <= 4:
                print(x / y, end=' ')
            else:
                print('')

# Idiomatic
import operator as op

def print_table(operator):
    for x in range(0,5):
        for y in range(0, 5):
            if x <= 4:
                print(str(operator(x, y)), end=' ')
            else:
                print('')

for operator in (op.add, op.sub, op.mul, op.itruediv):
    print_table(operator)
