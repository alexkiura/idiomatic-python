"""Idiomatic ways of writing for loops."""

# Scenario 1: having an index variable in a for loop
# harmful
my_container = ['Larry', 'Moe', 'Curly']
index = 0
for element in container:
    print('{}{}'.format(index, element))
    index += 1

# Idiomatic
my_container = ['Larry', 'Moe', 'Curly']
for index, element in enumerate(my_container):
    print('{}{}'.format(index, element))


# Scenario 2: iterating over an iterable using the in keyword
# harmful
my_list = ['Larry', 'Moe', 'Curly']
index = 0
while index < len(my_list):
    print(my_list[index])
    index += 1

# Idiomatic
my_list = ['Larry', 'Moe', 'Curly']
for element in my_list:
    print(element)


# Scenario 3: using else to execute code after a for loop concludes
# harmful
for user in get_all_users():
    has_malformed_email_address = False
    print('Checking {}'.fomat(user))
    for email_address in user.email_addresses:
        if email_is_malformed(email_address):
            print('Has a malformed email address')
            break
    if not has_malformed_email_address:
        print('All email addesses are valid')


# idiomatic
for user in get_all_users():
    print('Checking {}'.format(user))
    for email in user.email_addresses:
        if email_is_malformed(email):
            print('Has a malformed email address')
            break
    else:
        print('All email addesses are valid')
