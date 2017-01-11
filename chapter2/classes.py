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
