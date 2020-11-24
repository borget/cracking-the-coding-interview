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
# 21 / 21 test cases passed.
# Status: Accepted
# Runtime: 96 ms
# Memory Usage: 18.1 MB
from collections import Counter
def topKFrequent(nums, k):
    hash_counting = Counter(nums)
    bucket_max = hash_counting.most_common(1)
    bucket_len = max(bucket_max[0][1], len(hash_counting))
    bucket = [None] * bucket_len
    for h in hash_counting:
        if bucket[hash_counting[h]-1] is None:
            bucket[hash_counting[h] - 1] = []
            bucket[hash_counting[h] - 1].append(h)
        else:
            bucket[hash_counting[h]-1].append(h)
    # result = [b for b in reversed(bucket) if b is not None]
    res = []
    for r in reversed(bucket):
        if r is not None:
            for f in r:
                if len(res) < k:
                    res.append(f)
    return res


if __name__ == '__main__':
    print(topKFrequent([1,2], 2))
    print(topKFrequent([-1,-1], 1))
    print(topKFrequent([13,15,15,7,7,7,7, 7, 7, 7, 9, 9, 11, 6, 6, 6, 6, 12, 12, 12, 12, 12], 3))
    print(topKFrequent([3, 0, 1, 0], 1))
    print(topKFrequent([1], 1))
    print(topKFrequent([1, 2], 2))
