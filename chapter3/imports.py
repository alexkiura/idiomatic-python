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