"""Writing Idiomatic code by managing scripts better."""

# Scenario 5: using __init__.py to simplify package interfaces
# Harmful

# If the Gizmo directory has an empty __init__.py file

# Client code
from gizmo.client.interface import Gizmo
from gizmo.client.contrib.utils import GizmoHelper

# Idiomatic

# __init__.py code
from gizmo.client.interface import Gizmo
from gizmo.client.contrib.utils import GizmoHelper

# Client code
from gizmo import Gizmo, GizmoHelper

# Scenario 6: using if__name__ == __main to allow both importing and execution
# Harmful
import os
import sys

FIRST_NUMBER = float(sys.argv[1])
SECOND_NUMBER = float(sys.argv[2])

def divide(a, b):
    return a / b


# Every time this module is imported the code below is executed
if SECOND_NUMBER != 0:
    print(divide(FIRST_NUMBER, SECOND_NUMBER))


# Idiomatic
import os
import sys


def divide(a, b):
    return a / b

if __name__ == '__main__':
    first_number = sys.argv[1]
    second_number = sys.argv[2]

    if second_number != 0:
        print(divide(first_number, second_number))


# Scenario 7: Making python scripts directly executable

# Idiomatic
# Adding a shebang to make the script directly executable
#! /usr/bin/env python

# Scenario 8: using sys.exit to return proper exit codes
# Harmful
if __name__ == '__main__':
    import sys
    # What happens if no args are passed on the command line?
    if len(sys.argv) > 1:
        argument = sys.argv[1]
        result = do_stuff(argument)

        if result:
            do_stuff_with_result(result)


# Idiomatic
def main():
    import sys
    if len(sys.argv) < 2:
        sys.exit('You forgot to pass an argument')
    argument = sys.argv[1]
    result = do_stuff(argument)
    if not result:
        sys.exit(1)
    do_stuff_with_result(result)
    return 0

if __name__ == '__main__':
    sys.exit(main())