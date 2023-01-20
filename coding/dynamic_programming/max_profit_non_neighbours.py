def max_profit(arr):
    if not arr or len(arr) == 0:
        return 0

    n = len(arr)
    pick = arr[0]
    dont_pick = 0

    for ind in range(1, n):
        pick, dont_pick = dont_pick + arr[ind], max(dont_pick, pick)
        print(pick)
        print(dont_pick)

    return max(pick, dont_pick)


if __name__ == '__main__':
    print(max_profit([5, 1, 3, 11]))

    print(max_profit([2, 3, 2]))

    print(max_profit([1, 2, 3, 1]))


