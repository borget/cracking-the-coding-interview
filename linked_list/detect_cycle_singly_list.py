# This is a sample Python script.

# Press ⇧F10 to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def detectCycle(head: ListNode) -> ListNode:
    h = head
    if not head or not head.next:
        return None
    visited = dict()
    while h:
        if id(h) not in visited:
            visited[id(h)] = None
        else:
            return h
        h = h.next


if __name__ == '__main__':
    head = ListNode(1)
    # item1 = ListNode(2)
    # head.next = item1
    # item2 = ListNode(0)
    # item1.next = item2
    # item3 = ListNode(-4)
    # item2.next = item3
    # item3.next = item1

    result = detectCycle(head=head)
    print(result)

