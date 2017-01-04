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


# Scenario 2: use _ as a placeholder for data in a tuple that should be ignored
# harmful
(name, age, temp, temp2) = get_user_info(user)
if age > 21:
    output = '{name} can drink!'.format(name=name)
    # notice temp 1 and temp 2 are never used
    # use an _ as shown below

(name, age, _, _) = get_user_info(user)
if age > 21:
    output = '{name} can drink!'.format(name=name)
    # using _, we don't have to define temp variables

# Scenario 3: using tuples to unpack data
# harmful
list_from_csv_file = ['dog', 'Fido', 10]
animal = list_from_csv_file[0]
name = list_from_csv_file[1]
age = list_from_csv_file[2]
output = ('{name} the {animal} is {age} years old'.format(
    animal=animal, name=name, age=age))

# Idiomatic
list_from_csv_file = ['dog', 'Fido', 10]
(animal, name, age) = list_from_csv_file
output = ('{name} the {animal} is {age} years old'.format(
    animal=animal, name=name, age=age))

# Scenario 4: using tuples to return multiple values from a function
# harmful
from collections import Counter
STATS_FORMAT = """Statistics:
Mean: {mean}
Median: {median}
Mode: {mode}"""

def calculate_mean(value_list):
    return float(sum(value_list) / len(value_list))

def calculate_median(value_list):
    return value_list[int(len(value_list) / 2)]

def calculate_mode(value_list):
    return Counter(value_list).most_common(1)[0][0]

values = [10, 20, 20, 30]
mean = calculate_mean(values)
median = calculate_median(values)
mode = calculate_mode(values)
print(STATS_FORMAT.format(mean=mean, median=median, mode=mode))

# Idiomatic
from collections import Counter
STATS_FORMAT = """Statistics:
Mean: {mean}
Median: {median}
Mode: {mode}"""

def calculate_statistics(value_list):
    mean = float(sum(value_list) / len(value_list))
    median = value_list[int(len(value_list) / 2)]
    mode = Counter(value_list).most_common(1)[0][0]
    return (mean, median, mode)

(mean, median, mode) = calculate_statistics([10, 20, 20, 30])
print(STATS_FORMAT.format(mean=mean, median=median, mode=mode))
