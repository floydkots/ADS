from unittest import TestCase
from .search_insert import search_insert


class TestSearchInsert(TestCase):
    def test_0_finds_item(self):
        self.assertEqual(2, search_insert([1, 3, 5, 6], 5))

    def test_1_finds_index_of_missing(self):
        self.assertEqual(1, search_insert([1, 3, 5, 6], 2))

    def test_2_finds_index_of_missing_after(self):
        self.assertEqual(4, search_insert([1, 3, 5, 6], 7))

    def test_3_finds_index_of_missing_before(self):
        self.assertEqual(0, search_insert([1, 3, 5, 6], 0))

    def test_4_returns_0_for_empty_array(self):
        self.assertEqual(0, search_insert([], 0))

    def test_5_returns_correct_for_tricky(self):
        self.assertEqual(5, search_insert([0, 1, 2, 3, 4, 5, 6, 7, 8], 5))
        self.assertEqual(5, search_insert([0, 1, 2, 3, 4, 6, 7, 8, 9], 5))
