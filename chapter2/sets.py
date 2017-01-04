"""Idiomatic ways of dealing with sets."""

# Scenario 1: using sets to manipulate lists
# harmful
def get_both_popular_and_active_users():
    # Assume both functions return a list of users
    most_popular_users = get_most_popuar_users()
    most_active_users = get_most_active_users()
    polupar_and_active_users = []
    for user in most_active_users:
        if user in most_popular_users:
            polupar_and_active_users.append(user)
    return polupar_and_active_users


# Idiomatic
def get_both_popular_and_active_users():
    # Assume both functions return a list of users
    return set(get_most_active_users()) & set(get_most_popuar_users())


# Scenario 2: using set comprehensions to consisely generate sets
# harmful
users_first_names = set()
for user in users:
    users_first_names.add(user.first_name)

# Idiomatic
users_first_names = {user.first_name for user in users}

# Scenario 3: using sets to eliminate duplicate entries
# harmful
unique_surnames = []
# Generating a list of unique user names
for surname in surnames:
    if surname not in unique_surnames:
        unique_surnames.append(surname)

def display(elements, output_format='html'):
    if output_format == 'std_out':
        for element in elements:
            print(element)
    elif output_format == 'html':
        as_html = '<ul>'
        for element in elements:
            as_html += '<li>{}</li>'.format(element)
        return as_html + '</ul>'
    else:
        raise RuntimeError('Uknown format {}'.format(output_format))

# Idiomatic
unique_surnames = set(surnames)

def display(elements, output_format='html'):
    if output_format == 'std_out':
        for element in elements:
            print(element)
    elif output_format == 'html':
        as_html = '<ul>'
        for element in elements:
            as_html += '<li>{}</li>'.format(element)
        return as_html + '</ul>'
    else:
        raise RuntimeError('Uknown format {}'.format(output_format))
