from unittest import TestCase
from prime_numbers import is_prime


class PrimeNumberTests(TestCase):
    """Check if prime number generator outputs prime numbers"""
    def test_if_number_is_prime(self):
        self.assertEqual(is_prime(1), False)

    def test_if_number_is_prime2(self):
        self.assertEqual(is_prime(7), True)

