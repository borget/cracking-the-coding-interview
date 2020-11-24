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
    prev = head
    left = head
    right = head.next
    has_duplicate = False
    duplicate_val = None
    init_duplicate = False
    if left.val == right.val:
        init_duplicate = True
    while curr:
        if not right:
            break
        if left.val == right.val and not has_duplicate:
            has_duplicate = True
            duplicate_val = right.val
            left = prev
            right = right.next
            curr = right
        elif has_duplicate and duplicate_val == right.val:
            right = right.next
            curr = right
        elif has_duplicate and duplicate_val != right.val:
            has_duplicate = False
            prev.next = right
            left = right
            right = right.next
            curr = curr.next
        elif left.val != right.val:
            prev = left
            left = right
            right = right.next
            curr = left
    if has_duplicate:
        prev.next = None
    if head.next is None and init_duplicate:
        return None
    elif head.next and init_duplicate:
        head = head.next
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

    i1 = ListNode(1)
    i2 = ListNode(1)
    i3_1 = ListNode(1)
    i3_2 = ListNode(2)
    i4_1 = ListNode(3)
    i1.next = i2
    i2.next = i3_1
    i3_1.next = i3_2
    i3_2.next = i4_1

    result = deleteDuplicates(head=i1)

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


