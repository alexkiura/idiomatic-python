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
