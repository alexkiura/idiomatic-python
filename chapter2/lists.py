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

# Scenatio 3: preferring list comprehensions to map and filter
# harmful
the_list = list(range(1, 11))
def is_odd(number):
    return number % 2 == 1

odd_numbers = filter(is_odd, the_list)
odd_numbers_times_two = list(map(lambda x: x * 2, odd_numbers))

# Idiomatic
the_list = list(range(1, 11))
odd_numbers_times_two = [n * 2 for n in the_list if n % 2 == 1]

# Scenario 4: using the inbuilt function sum to sum elements of a list
# harmful
the_list = list(range(1, 11))
the_sum = 0
for element in the_list:
    the_sum += element

# Idiomatic
the_list = list(range(1, 11))
the_sum = sum(the_list)

# Scenario 5: using all to check if all elements of an iterable are true
# harmful
def contains_zero(iterable):
    for element in iterable:
        if element == 0:
            return True
    return False

# Idiomatic
def contains_zero(iterable):
    # 0 is falsy so all(iterable) works?
    return not all(iterable)

# Scenario 6: using * to represent the rest of a list
# harmful
some_list = ['a', 'b', 'c', 'd', 'e']
first, second, rest = some_list[0], some_list[1], some_list[2:]
print(rest)
first, middle, last = some_list[0], some_list[1: -1], some_list[-1]
print(middle)
head, penultimate, last = some_list[:-2], some_list[-2], some_list[-1]
print(head)

# Idiomatic
some_list = ['a', 'b', 'c', 'd', 'e']
first, second, *rest = some_list
print(rest)
first, *middle, last = some_list
print(middle)
*head, penultimate, last = some_list
head
