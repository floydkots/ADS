from unittest import TestCase
from .remove_duplicates import remove_duplicates


class TestRemoveDuplicates(TestCase):
    def test_a_returns_length_of_array_without_duplicates(self):
        self.assertEqual(2, remove_duplicates([1, 2]))

    def test_b_returns_correct_length_where_duplicates(self):
        self.assertEqual(2, remove_duplicates([1, 1, 2]))
        self.assertEqual(4, remove_duplicates([1, 2, 2, 3, 3, 3, 4, 4, 4]))
        self.assertEqual(2, remove_duplicates([1, 1, 1, 2]))
        self.assertEqual(2, remove_duplicates([1, 2, 2]))
        self.assertEqual(3, remove_duplicates([-1, 0, 0, 0, 0, 3, 3]))

    def test_c_returns_1_for_single_element_array(self):
        self.assertEqual(1, remove_duplicates([1]))

    def test_d_returns_1_for_all_same_int_array(self):
        self.assertEqual(1, remove_duplicates([1, 1, 1]))
