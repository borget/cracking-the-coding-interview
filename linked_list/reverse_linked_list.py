# Reverse a singly linked list.
#
# Example:
#
# Input: 1->2->3->4->5->NULL
# Output: 5->4->3->2->1->NULL
#Follow up:
#A linked list can be reversed either iteratively or recursively. Could you implement both?


from typing import List
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        init = head
        h = init
        while  init.next is not None:
            nxt = init.next
            init.next = nxt.next
            nxt.next = h
            h = nxt
        return h

if __name__ == "__main__":
    s = Solution()
    i5 = ListNode(val=5)
    i4 = ListNode(val=4, next=i5)
    i3 = ListNode(val=3, next=i4)
    i2 = ListNode(val=2, next=i3)
    i1 = ListNode(val=1, next=i2)

    result = s.reverseList(None)
    assert result == []
