# Matrix A, consisting of N rows and N columns of non-negative integers, is given.
# Rows are numbered from 0 to N−1 (from top to bottom). Columns are numbered from 0 to N−1 (from left to right).
# We would like to find a path that starts at the upper-left corner (0, 0) and, moving only right and down,
# finishes at the bottom-right corner (N−1, N−1). Then, all the numbers on this path will be multiplied together.
#
# Find a path such that the product of all the numbers on the path contain the minimal number of trailing zeros.
# We assume that 0 has 1 trailing zero.
#
# Write a function:
#
# def solution(A)
#
# that, given matrix A, returns the minimal number of trailing zeros.
#
# Examples:
#
# 1. Given matrix A below:
#
# The picture describes the first example test.
# the function should return 1. The optimal path is: (0,0) → (0,1) → (0,2) → (1,2) → (2,2) → (2,3) → (3,3).
# The product of numbers 2, 10, 1, 4, 2, 1, 1 is 160, which has one trailing zero.
# There is no path that yields a product with no trailing zeros.
#
# 2. Given matrix A below:
#
# The picture describes the second example test.
#
# the function should return 2. One of the optimal paths is: (0,0) → (1,0) → (1,1) → (1,2) → (2,2) → (3,2) → (3,3).
# The product of numbers 10, 1, 1, 1, 10, 1, 1 is 100, which has two trailing zeros.
# There is no path that yields a product with fewer than two trailing zeros.
#
# 3. Given matrix A below:
#
# The picture describes the third example test.
#
# the function should return 1. One of the optimal paths is: (0,0) → (0,1) → (1,1) → (1,2) → (2,2).
# The product of numbers 10, 10, 0, 10, 10 is 0, which has one trailing zero.
# There is no path that yields a product with no trailing zeros.
#
# Write an efficient algorithm for the following assumptions:
#
# N is an integer within the range [1..500];
# each element of matrix A is an integer within the range [0..1,000,000,000]
import heapq as pq


def is_valid_move(current, moves, move, n):
    m = moves[move]
    row = current[0] + m[0]
    col = current[1] + m[1]
    if row > n or col > n:
        return None
    return tuple((row, col))


def trailing_zero_cnt(product):
    num = str(product)
    count = 0
    for i in reversed(num):
        if i == '0':
            count += 1
        else:
            return count
    return 1 if count == 0 else count


def solution(A):
    elements = []
    moves = {'right': (0, 1), 'down': (1, 0)}
    visited = {(0, 0): A[0][0]}
    n = len(A)-1
    destiny = (n, n)
    pq.heappush(elements, (0, (0, 0)))
    while len(elements) > 0:
        current = pq.heappop(elements)
        c_pos = current[1]
        c_product = visited[c_pos]
        if c_pos == destiny:
            return trailing_zero_cnt(visited[c_pos])
        for move in moves:
            new = is_valid_move(c_pos, moves, move, n)
            if new and new not in visited:
                new_product = A[new[0]][new[1]]
                visited[new] = c_product * new_product
                zero_count = trailing_zero_cnt(c_product * new_product)
                pq.heappush(elements, (zero_count, (new[0], new[1])))
    return None


if __name__ == '__main__':
    test_grid = [[2, 10, 1, 3],
                 [10, 5, 4, 5],
                 [2, 10, 2, 1],
                 [25, 2, 5, 1]]
    result = solution(test_grid)
    print(result)
    assert result == 1

    test_grid = [[10, 1, 10, 1],
                 [1, 1, 1, 10],
                 [10, 1, 10, 1],
                 [1, 10, 1, 1]]
    result = solution(test_grid)
    print(result)
    assert result == 2

    test_grid = [[10, 10, 10],
                 [10, 0, 10],
                 [10, 10, 10]]
    result = solution(test_grid)
    print(result)
    assert result == 1

    test_grid = [[10, 10, 10],
                 [10, 0, 10],
                 [10, 10, 10]]
    result = solution(test_grid)
    print(result)
    assert result == 1

    test_grid = [[10]]
    result = solution(test_grid)
    print(result)
    assert result == 1