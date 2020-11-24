# This is a sample Python script.
from collections import deque
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def deleteDuplicates(head: ListNode) -> ListNode:
    queue = []
    if head is None:
        return head
    if (head and head.val is None) or (head.next is None):
        return head
    curr = head
    if curr.val != curr.next.val:
        queue.append(head)
        queue.append(head.next)
    else:
        init_dup = curr.val
        while len(queue) < 2:
            if not curr:
                break
            if curr.val != init_dup:
                queue.append(curr)
                init_dup = curr.val
            curr = curr.next
    if len(queue) == 0:
        return None
    elif len(queue) < 2:
        return ListNode(queue[0])
    elif len(queue) == 2 and curr is None:
        item1 = ListNode(queue[0].val)
        item2 = ListNode(queue[1].val)
        item1.next = item2
        return item1
    elif len(queue) == 2 and curr:
        curr = curr.next.next
    duplicate = False
    while curr:
        if queue[1].val != curr.val and not duplicate:
            queue[0] = queue[1]
            queue[1] = curr
            curr = curr.next
        elif queue[1].val != curr.val and duplicate:
            duplicate = False
            queue[0].next = curr
            queue[1] = curr
        else:
            duplicate = True
            if not curr.next:
                queue[0].next = None
            curr = curr.next
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
    i3_1.next = i4_1
    i3_1.next = i3_2
    i3_2.next = i4_1
    i4_1.next = i4_2
    i4_2.next = i5

    #Input: 1->1->1->2->3
    #Output: 2->3

    result = deleteDuplicates(head=i1)
    print(result)

