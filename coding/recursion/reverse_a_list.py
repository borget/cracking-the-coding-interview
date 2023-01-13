from collections import deque

def reverse(nums):
    if len(nums) == 0:
        return
    item = nums.pop()
    reverse(nums)
    nums.appendleft(item)

def reverseString(list):
    if len(list) == 0:
        return
    pop = list[0]
    del list[0]
    reverseString(list)
    list.append(pop)

if __name__ == '__main__':
    l = deque([1, 2, 3, 4, 5])
    reverse(l)
    print(l)
    input = ["h","e","l","l","o"]
    reverseString(input)
    print(input)