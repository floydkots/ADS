from unittest import TestCase
from .roman_to_integer import roman_to_int


class TestRomanToInteger(TestCase):
    def test_roman_to_int_single_numeral(self):
        self.assertEqual(1, roman_to_int('I'))
        self.assertEqual(5, roman_to_int('V'))
        self.assertEqual(10, roman_to_int('x'))
        self.assertEqual(50, roman_to_int('L'))
        self.assertEqual(100, roman_to_int('C'))
        self.assertEqual(500, roman_to_int('D'))
        self.assertEqual(1000, roman_to_int('m'))

    def test_roman_to_int_subtractive_notation(self):
        self.assertEqual(4, roman_to_int('IV'))
        self.assertEqual(1904, roman_to_int('MCMIV'))
