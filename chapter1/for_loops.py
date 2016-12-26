"""Idiomatic ways of writing for loops."""
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
