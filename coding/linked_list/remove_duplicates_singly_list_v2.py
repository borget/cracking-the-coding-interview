# This is a sample Python script.
from collections import deque
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def deleteDuplicates(head: ListNode) -> ListNode:
    curr = head
    if not head or not head.next:
        return head
    while curr:
        if curr.val == curr.next.val:
            pass

    return head


if __name__ == '__main__':
    #  Input: 1->2->3->3->4->4->5
    # Output: 1->2->5
    i1 = ListNode(1)
    i2 = ListNode(2)
    i3_1 = ListNode(3)
    i3_2 = ListNode(3)
    i4_1 = ListNode(4)
    i4_2 = ListNode(4)
    i5 = ListNode(5)
    i1.next = i2
    i2.next = i3_1
    i3_1.next = i3_2
    i3_2.next = i4_1
    i4_1.next = i4_2
    i4_2.next = i5

    result = deleteDuplicates(head=i1)
    print(result)

