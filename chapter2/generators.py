"""Using generators to write more idiomatic code."""

# Scenario 1: preferring generator expressions to list expressions

# Harmful

for upper_case_name in [name.upper() for name in get_all_usernames()]:
    process_username(upper_case_name)

# Idiomatic
for upper_case_name in (name.upper() for name in get_all_usernames()):
    process_username(upper_case_name)

