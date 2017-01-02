"""Idiomatic ways of dealing with lists."""

# Scenario 1: using list comprehension to transform an existing list
# harmful
some_other_list = range(10)
some_list = list()
for element in some_other_list:
    if is_prime(element):
        some_list.append(element + 5)

# Idiomatic
some_other_list = range(10)
some_list = [element + 5 for element in some_other_list if is_prime(element)]

# Scenario 2: making use of negative indices
# harmful
def get_suffix(word):
    word_length = len(word)
    return word[word_length - 2:]
# shorter harmful
def get_suffix(word):
    word_length = len(word)
    return [len(word) - 2:]

# Idiomatic
def get_suffix(word):
    return word[-2:]
