from unittest import TestCase
from .strstr import str_str


class TestStrStr(TestCase):
    def test_0_finds_character_string(self):
        self.assertEqual(0, str_str('a', ''))
        self.assertEqual(3, str_str('floyd', 'y'))
        self.assertEqual(2, str_str('hello', 'll'))
        self.assertEqual(3, str_str('hello', 'lo'))

    def test_1_returns_neg_1_if_not_found(self):
        self.assertEqual(-1, str_str('aaaaa', 'bba'))

    def test_2_finds_tricky_strings(self):
        self.assertEqual(5, str_str('lalallo', 'lo'))
        self.assertEqual(0, str_str('lalallo', 'la'))
        self.assertEqual(-1, str_str('aaa', 'aaaa'))

    def test_3_recursion_in_mississippi_land(self):
        self.assertEqual(4, str_str('mississippi', 'issip'))
        self.assertEqual(6, str_str('mississippi', 'sipp'))
        self.assertEqual(-1, str_str('mississippi', 'issipi'))

