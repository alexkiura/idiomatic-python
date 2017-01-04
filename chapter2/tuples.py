"""Idiomatic ways of dealing with lists."""

# Scenario 1: used named tuples to make tuple-heavy code more clear
# Assume the employees table has the following columns:
# first_name, last_name, department, manager, salary, hire_date (in that order)


# harmful
def print_employee_information(db_connection):
    db_cursor = db_connection.cursor()
    results = db_cursor.execute('select * from employees').fetchall()
    for row in results:
        # it's very hard to follow what's being printed
        print(row[1] + ', ' + row[0] + ' was hired on ' + row[5] +
              row[5] + ' (for $' + row[4] + ' per annum) '
              ' into the ' + row[2] + ' department and reports to ' + row[3])

# Idiomatic
from collections import namedtuple
EmployeeRow = namedtuple('EmployeeRow', ['first_name',
                                         'last_name,' 'department',
                                         'manager', 'salary', 'hire_date'])

EMPLOYEE_INFO_FORMAT = '{last_name}, {first_name} was hired on {hire_date}\
    (for ${salary} per annum) into the {department} department and reports\
    to {manager}'

def print_employee_information(db_connection):
    db_cursor = db_connection.cursor()
    results = db_cursor.execute('select * from employees').fetchall()
    for result in results:
        employee = EmployeeRow._make(row)
        print(EMPLOYEE_INFO_FORMAT.format(**employee._asdict()))