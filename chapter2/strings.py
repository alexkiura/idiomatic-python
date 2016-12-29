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
