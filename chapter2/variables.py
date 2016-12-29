"""Idiomatic ways of dealing with variables."""

# Scenario 1: using multiple assignment to condense variables all set to same
# value
# harmful
x = 'foo'
y = 'foo'
z = 'foo'

# Idiomatic
x = y = z = 'foo'

# Scenario 2: using a temporary variable when swapping two variables
# harmful
foo = 'Foo'
bar = 'Bar'
temp = foo
foo = bar
bar = temp

# Idiomatic
foo = 'Foo'
bar = 'Bar'
foo, bar = bar, foo
