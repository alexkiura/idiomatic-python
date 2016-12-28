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
