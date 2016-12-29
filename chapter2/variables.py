"""Idiomatic ways of dealing with variables."""

# Scenario 1: using multiple assignment to condense variables all set to same
# value
# harmful
x = 'foo'
y = 'foo'
z = 'foo'

# Idiomatic
x = y = z = 'foo'
