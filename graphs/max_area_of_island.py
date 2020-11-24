# 695. Max Area of Island
# Medium
# Given a non-empty 2D array grid of 0's and 1's, an island is a group of 1's (representing land)
# connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.
#
# Find the maximum area of an island in the given 2D array. (If there is no island, the maximum area is 0.)
#
# Example 1:
#
# [[0,0,1,0,0,0,0,1,0,0,0,0,0],
#  [0,0,0,0,0,0,0,1,1,1,0,0,0],
#  [0,1,1,0,1,0,0,0,0,0,0,0,0],
#  [0,1,0,0,1,1,0,0,1,0,1,0,0],
#  [0,1,0,0,1,1,0,0,1,1,1,0,0],
#  [0,0,0,0,0,0,0,0,0,0,1,0,0],
#  [0,0,0,0,0,0,0,1,1,1,0,0,0],
#  [0,0,0,0,0,0,0,1,1,0,0,0,0]]
# Given the above grid, return 6. Note the answer is not 11, because the island must be connected 4-directionally.
# Example 2:
#
# [[0,0,0,0,0,0,0,0]]

# positions
# [[(0,0), (0,1), (0,2)],
#  [(1,0), (1,1), (1,2)],
#  [(2,0), (2,1), (2,2)]]
# Submission Detail
# 726 / 726 test cases passed.
# Status: Accepted
# Runtime: 188 ms
# Memory Usage: 14.4 MB
# Submitted: 0 minutes ago


from typing import List
from collections import deque


class Solution:
    def __init__(self):
        self.wind_rose_offset = {'up': (-1, 0), 'right': (0, 1), 'down': (1, 0), 'left': (0, -1)}
        self.ISLAND = 1

    def valid_pos(self, neighbour, grid):
        if neighbour[0] < 0 or neighbour[1] < 0:
            return False
        rows_len = len(grid)
        cols_len = len(grid[0])
        if neighbour[0] > rows_len - 1 or neighbour[1] > cols_len - 1:
            return False
        return tuple((neighbour[0], neighbour[1]))

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0
        queue = deque()
        for i, i_item in enumerate(grid):
            for j, j_item in enumerate(i_item):
                current_island = (i, j)
                if grid[i][j] == self.ISLAND:
                    grid[i][j] = 0
                    queue.append(current_island)
                    new_max_area = 1
                    while len(queue) > 0:
                        q = queue.pop()
                        for w in self.wind_rose_offset:
                            offset = self.wind_rose_offset[w]
                            neighbour = (q[0] + offset[0], q[1] + offset[1])
                            valid_pos = self.valid_pos(neighbour, grid)
                            if valid_pos and grid[valid_pos[0]][valid_pos[1]] == self.ISLAND:
                                grid[valid_pos[0]][valid_pos[1]] = 0
                                queue.append(neighbour)
                                new_max_area += 1
                    if new_max_area > max_area:
                        max_area = new_max_area
        return max_area


if __name__ == '__main__':
    test_grid = [[0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
                 [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
                 [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]]
    obj = Solution()
    result = obj.maxAreaOfIsland(test_grid)
    assert result == 6
    print(result)
    test_grid = [[0, 0, 0, 0, 0, 0, 0, 0]]
    obj = Solution()
    result = obj.maxAreaOfIsland(test_grid)
    assert result == 0
    print(result)
