from unittest import TestCase
from .reverse_integer import reverse, reverse_2


class TestReverseInteger(TestCase):
    def test_reverses_positive_integer(self):
        self.assertEqual(321, reverse(123))

    def test_reverses_negative_integer(self):
        self.assertEqual(-321, reverse(-123))

    def test_reverses_and_ignores_initial_zeros(self):
        self.assertEqual(21, reverse(120))

    def test_reverses_zero(self):
        self.assertEqual(0, reverse(0))

    def test_returns_zero_in_case_of_simulated_overflow(self):
        self.assertEqual(0, reverse(1534236469))


class TestReverseInteger2(TestCase):
    def test_reverses_positive_integer(self):
        self.assertEqual(321, reverse_2(123))

    def test_reverses_negative_integer(self):
        self.assertEqual(-321, reverse_2(-123))

    def test_reverses_and_ignores_initial_zeros(self):
        self.assertEqual(21, reverse_2(120))

    def test_reverses_zero(self):
        self.assertEqual(0, reverse_2(0))

    def test_returns_zero_in_case_of_simulated_overflow(self):
        self.assertEqual(0, reverse_2(1534236469))

