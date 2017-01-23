"""Writing tests in an idiomatic way."""

import unittest

def add_mumbers(first_number, second_number):
    """"
    Return the sum of two numbers.

    Arguments:
        first_number
        second_number
    """
    return first_number + second_number

def increment(number, step=1):
    """
    Increment a number by a given n steps.

    The default step is 1."""
    return number + step

def get_divisors_of_prime_numbers(prime):
    """Returns None for everything."""
    prime = None
    return prime


# Harmful
class Test(unittest.TestCase):
    """A random test case."""

    def test_adding_positive_ints(self):
        """Test adding two numbers."""
        self.assertTrue(add_mumbers(2, 2,), 4)

    def test_increment(self):
        """Does increment return a value Greater than what was passed?"""
        self.assertTrue(increment(2) > 2)

    def test_diviors_of_prime_numbers(self):
        self.assertTrue(get_divisors_of_prime_numbers(11) is None)


# Idiomatic
class Test2(unittest.TestCase):
    """.A random test case."""
    def test_adding_positive_ints(self):
        self.assertEqual(add_mumbers(3, 3), 6)

    def test_increment(self):
        self.assertGreater(increment(3), 3)

    def test_divisors_of_prime_numbers(self):
        self.assertIsNone(get_divisors_of_prime_numbers(11))
    