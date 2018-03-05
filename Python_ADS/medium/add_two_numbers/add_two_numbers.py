# Definition for singly-linked list.


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        if self.next:
            return str(self.val) + ' -> ' + str(self.next)
        else:
            return str(self.val)


def add_two_numbers(l1, l2):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """
    current_l1 = l1
    current_l2 = l2
    result = current_l3 = ListNode(0)
    total = 0

    while current_l1 or current_l2:
        total //= 10
        if current_l1:
            total += current_l1.val
            current_l1 = current_l1.next
        if current_l2:
            total += current_l2.val
            current_l2 = current_l2.next

        current_l3.next = ListNode(total % 10)
        current_l3 = current_l3.next

    if total // 10 == 1:
        current_l3.next = ListNode(1)
    return result.next
