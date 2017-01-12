"""Idiomatic ways of writing classes."""

# Scenarion 1: using self or @classmethod when referring to class attributes

# harmful
class Blog():
    __tablename__ = 'Blog'

    def table_name(self):
        return Blog.__tablename__


class DerivedBlog(Blog):
    __tablename__ = 'derived blog'

b = DerivedBlog()
print(b.table_name())  # prints blog


# Idiomatic
class Blog():
    __tablename__ = 'blog'

    def table_name(self):
        return self.__tablename__

    @classmethod
    def other_table_name(cls):
        return cls.__tablename__


class DerivedBlog():
    __tablename__ = 'derived blog'

b = DerivedBlog()
print(b.tablename())  # prints derived blog


# Scenario 2: using isinstance to determine the type of an object
# harmful
def get_size(some_object):
    """.Returns len(some_object) for iterables
    some_object for ints and floats
    1 for any other type
    """
    try:
        return len(some_object)

    except TypeError:
        if some_object in(True, False, type(None)):
            return 1

        else:
            return int(some_object)

# Idiomatic
def get_size(some_object):
    if isinstance(some_object, (list, dict, tuple, str)):
        return len(some_object)

    elif isinstance(some_object, (bool, type(None))):
        return 1

    elif isinstance(some_object, (int, float)):
        return int(some_object)

# Scenario 3: using leading underscores to denote private data:
# harmful
class Foo():
    def __init__(self):
        self.id = 8
        self.value = self.get_value()

    def get_value(self):
        pass

    def should_destroy_earth(self):
        return self.id == 42


class Baz(Foo):
    def get_value(self, some_new_parameter):
        """Creating a Baz instance fails because get_value is defined
        in the Base class __init__ method and the Base class definition takes
        no parameter.
        ."""
        pass


class Qux(Foo):
    """We are unaware of Foo's internals.
    We unknowingly create an instance attribute named id and set it to 42.
    This destroys the earth."""

    def __init__(self):
        super(Qux, self).__init__()
        self.id = 42

q = Qux()
b = Baz() # raises TypeError
q.should_destroy_earth() # returns True
q.id == 42 # returns True

# Idiomatic
class Foo():
    def __init__(self):
        """Since id is important, we make it a private variable"""
        self.__id = 8
        self.value = self.__get_value()

    def get_value(self):
        pass

    def should_destroy_earth(self):
        return self.__id == 42

    __get_value = get_value


class Baz(Foo):
    def get_value(self, some_new_parameter):
        pass

class Qux(Foo):
    def __init__(self):
        self.id = 42
        super(Qux, self).__init__()

q = Qux()
b = Baz() # does not raise TypeError
q.should_destroy_earth()
q.id == 42

# Scenrario 4: use properties to future proof class implementation
# harmful
class Product():
    def __init__(self, name, price):
        self.name = name
        self.price = price

# Idiomatic
class Product():
    def __init__(self, name, price):
        self.name = name
        self._price = price

    @property
    def price(self):
        return self._price * TAX_RATE

    @price.setter
    def price(self, value):
        self._price = value


# Scenario 5: using _repr_ for a machine-readable representation of the class
# harmful
class Foo():
    def __init__(self, bar=10, baz=12, cache=None):
        self.bar = bar
        self.baz = baz
        self._cache = cache or {}

    def __str__(self):
        return 'Bar is {}, Baz is {}'.format(self.bar, self.baz)


def log_to_console(instance):
    print(instance)

# instance
class Foo():
    def __init__(self, bar=10, baz=12, cache=None):
        self.bar = bar
        self.baz = baz
        self._cache = cache or {}

    def __str__(self):
        return '{}, {}'.format(self.bar, self.baz)

    def __repr__(self):
        return 'Foo({}, {}, {})'.format(self.bar, self.baz, self._cache)

def log_to_console(instance):
    print(instance)

# Scenario 6: using __str__ for a human readable representation
# harmful
class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y

# Idiomatic
class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return '({0}, {1})'.format(self.x, self.y)

p = Point(10, 15)
print(p)
