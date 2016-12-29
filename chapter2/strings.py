"""Idiomatic ways of dealing with strings."""

# Scenario 1: chaining functions to make transformations clear
# harmful
book_info = ' The Three Musketeers: Alexandre Dumas'
formatted_book_info = book_info.strip()
formatted_book_info = formatted_book_info.upper()
formatted_book_info = formatted_book_info.replace(':', ' by')

# Idiomatic
book_info = ' The Three Musketeers: Alexandre Dumas'
formatted_book_info = book_info.strip().upper().replace(':', ' by')

# Scenario 2: using ''.join when creating a single string for list elements
# harmful
result_list = ['True', 'False', 'File not found']
result_string = ''
for result in result_list:
    result_string += result

# Idiomatic
result_list = ['True', 'False', 'File not found']
result_string = ''.join(result_list)

# Scenario 3: using ord to get ASCII code of a char and vice versa
# harmful
hash_value = 0
character_hash = {
    'a': 97,
    'b': 98,
    'c': 99,
    # .....
    'y': 121,
    'z': 122,
}

for e in some_string:
    hash_value += ord(e)

return hash_value
