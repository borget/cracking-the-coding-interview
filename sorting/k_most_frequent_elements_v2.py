# Given a non-empty array of integers, return the k most frequent elements.
#
# Example 1:
#
# Input: nums = [1,1,1,2,2,3], k = 2
# Output: [1,2]
# Example 2:
#
# Input: nums = [1], k = 1
# Output: [1]
# Note:
#
# You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
# Your algorithm's time complexity must be better than O(n log n), where n is the array's size.
# It's guaranteed that the answer is unique, in other words the set of the top k frequent elements is unique.
# You can return the answer in any order.

def topKFrequent(nums, k):
    counter_set = {}
    for n in nums:
        if n in counter_set:
            counter_set[n] += 1
        else:
            counter_set[n] = 1
    top = sorted(counter_set.values())

    result = []
    max_iter = 0
    for x in top[::-1]:
        if max_iter == k:
            break
        idx = None
        for c in counter_set:
            if counter_set[c] == x:
                idx = c
                break
        if idx is not None:
            result.append(idx)
            del counter_set[c]
        max_iter += 1
    return result


if __name__ == '__main__':
    print(topKFrequent([7, 7, 7, 7, 9, 9, 11, 6, 6, 6, 6, 12, 12, 12, 12, 12], 3))
    print(topKFrequent([3, 0, 1, 0], 1))
    print(topKFrequent([1], 1))
    print(topKFrequent([1, 2], 2))
