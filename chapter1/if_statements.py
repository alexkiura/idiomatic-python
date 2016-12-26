"""Idiomatic ways of writing if statements."""

# Scenario 1: Chaining if statements
# harmful
if x <= y and y <= z:
    return True

# Idiomatic
if x <= y <= z:
    return True

# short hand


def compare_xyz(x, y, z):
    """Return True if y is greater than x but smaller than z."""
    return x <= y <= z

# Scenario 2: Placing conditional code after colon
# harmful
name = 'Jeff'
address = 'New York, NY'

if name: print(name)
print address

# Idiomatic
if name:
    pritn(name)
print(address)


# Scenario 3: repeating variable name in compound if statementn
# harmful
is_generic_name = False
name = 'Tom'
if name == 'Tom' or name == 'Dick' or name == 'Harry':
    is_generic_name = True

# Idiomatic
name = 'Tom'
is_generic_name = name in ('Tom', 'Dick', 'Harry')
