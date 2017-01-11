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
