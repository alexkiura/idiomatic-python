"""Wriring idiomatic code by better managing imports."""

# Scenario 1: Arranging impors in a standard order
# Harmful

# Some function and class definitions
import concurrent.futures
from flask import render_template


# Stuff using futures and Flask's render template
from flask import (Flask, request, session, g, redirect,url_for,
abort, render_template, flash, _app_ctx_stack)
import requests

# Code using Flask and requests
if __name__ == '__main__':
    import this_project.utilities.sentient_network as skynet
    import this_project.widgets
    import sys

# Idiomatic
import concurrent.futures
import os.path
import sys
from flask import (Flask, request, session, g, redirect,url_for,
    abort, render_template, flash, _app_ctx_stack)
import requests
import this_project.utilities.sentient_network as skynet
import this_project.widgets

# Scenario 2: Prefer absolute to relative imports
# Harmful
from ..package import other_module

# Idiomatic
import package.other_module
import package.other_module as other


# Scenario 3: Avoiding asterix '*' imports
# Harmful
from itertools import *

Idiomatic
from itertools import (compress permutations, count, cycle)

# Or
import itertools


# Scenario 4: Using a try block to determine if a package is available
# Harmful
import cProfile
# Uh-oh! The user does not have cProfile installed
print(cProfile.__all__)

# Idiomatic
try: 
    import cProfile as profiler
except:
    import profile as profiler

print(profiler.__all__)

# Scenario 5: Using tuples to organize long list of module to import
# Harmful
from django.db.models import AutoField, BigIntegerField, BooleanField, CharField
from django.db.models import CommaSeparatedIntegerField, DateField, DateTimeField

# Idiomatic
from django.db.models import (AutoField, BigIntegerField, BooleanField, CharField,
    CommaSeparatedIntegerField, DateField, DateTimeField)


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
