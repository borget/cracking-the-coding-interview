from queue import PriorityQueue
from typing import List


class Solution:
    """
    https://leetcode.com/problems/sort-an-array/description/
    Given an array of integers nums, sort the array in ascending order and return it.

    You must solve the problem without using any built-in functions in O(nlog(n))
    time complexity and with the smallest space complexity possible.
    """

    def sortArray(self, nums: List[int], reverse: bool = False) -> List[int]:
        q = PriorityQueue()
        for num in nums:
            q.put(num)

        result = []
        while not q.empty():
            next_item = q.get()
            result.append(next_item)

        if reverse:
            result.reverse()

        return result


if __name__ == '__main__':
    nums = [1, 0, 3]

    print(Solution().sortArray(nums, reverse=True))
