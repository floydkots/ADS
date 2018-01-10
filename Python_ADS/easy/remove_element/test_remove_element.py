from unittest import TestCase
from .remove_element import remove_element


class TestRemoveElement(TestCase):
    def test_a_returns_0_length_for_empty_array(self):
        self.assertEqual(0, remove_element([], 1))

    def test_b_returns_0_length_for_single_int(self):
        self.assertEqual(0, remove_element([1], 1))
        self.assertEqual(0, remove_element([2, 2], 2))
        self.assertEqual(0, remove_element([3, 3, 3], 3))

    def test_c_returns_correct_length_for_single_int_instance(self):
        self.assertEqual(2, remove_element([2, 1, 2], 1))
        self.assertEqual(2, remove_element([2, 2, 1], 1))
        self.assertEqual(2, remove_element([1, 2, 2], 1))
        self.assertEqual(2, remove_element([1, 1, 1, 2, 2], 1))
        self.assertEqual(1, remove_element([2, 2, 3], 2))
        self.assertEqual(1, remove_element([2, 2, 2, 2, 3], 2))

    def test_d_returns_correct_length_for_multi_int_instance(self):
        self.assertEqual(2, remove_element([2, 3, 3, 2], 2))
