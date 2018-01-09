from unittest import TestCase
from .valid_parentheses import is_valid


class TestValidParentheses(TestCase):
    def test_returns_false_for_string_with_odd_length(self):
        self.assertFalse(is_valid('['))
        self.assertFalse(is_valid('[]}'))

    def test_returns_false_for_valid_even_length_strings(self):
        self.assertFalse(is_valid('(('))
        self.assertFalse(is_valid('){'))

    def test_returns_true_for_valid_nested_parens(self):
        self.assertTrue(is_valid('([])'))
