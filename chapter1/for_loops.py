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
