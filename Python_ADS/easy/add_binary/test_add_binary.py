from unittest import TestCase
from .add_binary import add_binary


class TestAddBinary(TestCase):
    def test_adds_1_to_11(self):
        self.assertEqual('100', add_binary('11', '1'))

    def test_adds_1_to_0(self):
        self.assertEqual('1', add_binary('0', '1'))

    def test_adds_0_to_101(self):
        self.assertEqual('101', add_binary('0', '101'))

    def test_adds_11_to_1011(self):
        self.assertEqual('1110', add_binary('11', '1011'))

