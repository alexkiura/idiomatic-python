"""Organizing code to make it more idiomatic."""


# Scenario 1: Using capital letters when declaring global constant values
# Harmful
seconds_in_a_day = 60 * 60 *24

def display_uptime_percentage(uptime_in_seconds):
    percentage_run_time = (
        uptime_in_seconds /seconds_in_a_day) * 100

    return 'The process was up {percent} percent of the day'.format(
        percent=int(percentage_run_time))

# calculate uptime
uptime_in_seconds = 60 * 60 * 20
display_uptime_percentage(uptime_in_seconds)

# Idiomatic
SECONDS_IN_A_DAY = 60 * 60 * 24

def display_uptime_percentage2(uptime_in_seconds):
    percentage_run_time = (
        uptime_in_seconds / SECONDS_IN_A_DAY) * 100
    return 'The process was up {percent} percent of the day'.format(
        percent=int(percentage_run_time))


# Scenario 2: placing multiple statements on  single line
# Harmful
for element in my_list: print(element); print('----')

# Idiomatic
for element in my_list:
    print(element)
    print('-------')

# Scenario 3: Follow docstrings conventions in PEP-257
# Harmful
def calculate_statistics(value_list):
    # calculates various statistics for a list of numbers
    return (value_list,)

# Idiomatic
def calculate_statistics2(value_list):
    """Return a tuple containing mean, median and mode of a list of integers.

    Arguments:
    value_list-- a list of integer values
    """
    return (value_list,)


# Scenario 4: Using inline documentation sparingly
# Harmful
def calculate_mean(numbers):
    """Return the mean of a list of numbers."""

    # If the list is empty, we have no mean
    if not numbers:
        return 0

    # A variable to keep track of the running sum
    total = 0

    # Iterate over each number in the list
    for number in numbers:
        total += number

    # Divide the sum of all the numbers by the number of elements in the list
    return total / len(numbers)

# Idiomatic
def calculate_mean2(numbers):
    """Return the mean of a list of numbers."""
    return sum(numbers) / len(numbers)
