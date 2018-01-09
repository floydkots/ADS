from unittest import TestCase
from .longest_common_prefix import longest_common_prefix


class TestLongestCommonPrefix(TestCase):
    def test_returns_empty_string_for_empty_array(self):
        self.assertEqual('', longest_common_prefix([]))

    def test_returns_empty_string_for_array_with_empty_strings(self):
        self.assertEqual('', longest_common_prefix(['']))
        self.assertEqual('', longest_common_prefix(['', '']))

    def test_returns_empty_string_for_an_array_with_one_empty_string(self):
        self.assertEqual('', longest_common_prefix(['', 'aa']))

    def test_returns_longest_prefix(self):
        strings_1 = ['geeksforgeeks', 'geeks', 'geek', 'geezer']
        strings_2 = ['apple', 'ape', 'april']
        strings_3 = ["aa", "ab"]
        self.assertEqual('gee', longest_common_prefix(strings_1))
        self.assertEqual('ap', longest_common_prefix(strings_2))
        self.assertEqual('a', longest_common_prefix(strings_3))
        self.assertEqual('a', longest_common_prefix(['aa', 'a']))

