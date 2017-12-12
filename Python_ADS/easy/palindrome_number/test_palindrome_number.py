from unittest import TestCase

from .palindrome_number import is_palindrome


class TestPalindromeNumber(TestCase):
    def test_returns_false_for_negative_number(self):
        self.assertFalse(is_palindrome(-1))

    def test_returns_true_for_single_digit_number(self):
        self.assertTrue(is_palindrome(9))

    def test_returns_true_for_a_palindrome(self):
        self.assertTrue(is_palindrome(12321))

    def test_returns_false_for_a_non_palindrome(self):
        self.assertFalse(is_palindrome(5432354))

    def test_returns_false_for_two_digit_number(self):
        self.assertFalse(is_palindrome(10))

    def test_returns_false_for_non_palindrome_with_in_zeros(self):
        self.assertFalse(is_palindrome(1000021))

