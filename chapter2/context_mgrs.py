"""Idiomatic ways of managing resources."""

# Scenario 1: Use context managers to ensure resources are properly managed
# Harmful

def raise_exception(arg):
    """Does nothing."""
    return arg

def read_file():
    """Should read a file in a harmful way."""
    file_handle = open('path to file', 'r')
    for line in file_handle.readlines():
        if raise_exception(line):
            print('No! An exception')


# Idiomatic
def read_file_idiomatically():
    """Should read a file in an idomatic way."""
    with open('path to file', 'r') as file_handle:
        for line in file_handle:
            if raise_exception(line):
                print('No! An exception')
