# You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.
# Merge all the linked-lists into one sorted linked-list and return it.
# Definition for singly-linked list.
from typing import List
# Input: lists = [[1,4,5],[1,3,4],[2,6]]
# Output: [1,1,2,3,4,4,5,6]
# Explanation: The linked-lists are:
# [
#   1->4->5,
#   1->3->4,
#   2->6
# ]
# merging them into one sorted list:
# 1->1->2->3->4->4->5->6
import heapq as pq


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def init_pq(self, lists, pq_elements):
        for idx, i in enumerate(lists):
            node: ListNode = lists[idx]
            if node is not None:
                pq.heappush(pq_elements, (node.val, idx))

    def merge_items(self, merged, item, pq_, lists):
        node = lists[item[1]]
        smallest = item[0]
        cursor = merged
        while node is not None and node.val == smallest:
            cursor.next = ListNode(node.val, next=None)
            node = node.next
            cursor = cursor.next
        if node is not None:
            pq.heappush(pq_, (node.val, item[1]))
            lists[item[1]] = node
        return cursor

    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        merged: ListNode = ListNode(0, None)
        cursor = merged
        p_queue = []
        self.init_pq(lists, p_queue)
        if len(p_queue) == 0:
            return ListNode(val='')
        while len(p_queue) != 0:
            smallest = pq.heappop(p_queue)
            cursor = self.merge_items(cursor, smallest, p_queue, lists)
        return merged.next


if __name__ == '__main__':
    item1 = ListNode(1, next=ListNode(2, next=ListNode(2, next=None)))
    item2 = ListNode(1, next=ListNode(1, next=ListNode(2, next=None)))
    input_list = [item1, item2]
    solution = Solution()
    result = solution.mergeKLists(input_list)
    assert True == True


    node3 = ListNode(val=5, next=None)
    node2 = ListNode(val=4, next=node3)
    item1 = ListNode(val=1, next=node2)
    input_list = [item1]
    node3 = ListNode(val=4, next=None)
    node2 = ListNode(val=3, next=node3)
    item2 = ListNode(val=1, next=node2)
    input_list.append(item2)
    node2 = ListNode(val=6, next=None)
    item3 = ListNode(val=2, next=node2)
    input_list.append(item3)
    solution = Solution()
    result = solution.mergeKLists(input_list)
    # 1->1->2->3->4->4->5->6
    assert True

    solution = Solution()
    result = solution.mergeKLists([])
    assert True
    # []

    solution = Solution()
    list_ = []
    list_.append(ListNode(None, None))
    result = solution.mergeKLists(list_)
    assert True
    # [[]]

