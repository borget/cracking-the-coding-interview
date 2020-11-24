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
    result = []
    for top in range(k):
        if len(counter_set) > 0:
            t = getTop(counter_set)
            result.append(t)
            del counter_set[t]
        else:
            break
    return result

def getTop(counts):
    top1 = -1
    idx = None
    for c in counts:
        if top1 < counts[c]:
            top1 = counts[c]
            idx = c
    return idx


if __name__ == '__main__':
    print(topKFrequent([7, 7, 7, 7, 2, 2, 3, 1, 1, 1, 1, 0, 0, 0, 0, 0], 3))
    print(topKFrequent([1], 1))
