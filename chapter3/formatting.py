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