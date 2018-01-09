from unittest import TestCase
import copy
from .merge_two_sorted_lists import ListNode, merge_two_lists, merge_two_list_recursively


class TestMergeTwoLists(TestCase):
    def test_merges_in_correct_order(self):
        l11 = ListNode(1)
        l12 = ListNode(2)
        l14 = ListNode(4)
        l11.next = l12
        l12.next = l14
        l11copy = copy.deepcopy(l11)

        l21 = ListNode(1)
        l23 = ListNode(3)
        l24 = ListNode(4)
        l21.next = l23
        l23.next = l24
        l21copy = copy.deepcopy(l21)

        r1a = ListNode(1)
        r1b = ListNode(1)
        r2 = ListNode(2)
        r3 = ListNode(3)
        r4a = ListNode(4)
        r4b = ListNode(4)
        r1a.next = r1b
        r1b.next = r2
        r2.next = r3
        r3.next = r4a
        r4a.next = r4b

        print(l11)

        self.assertEqual(r1a, merge_two_lists(l11, l21))
        self.assertEqual(r1a, merge_two_list_recursively(l11copy, l21copy))
