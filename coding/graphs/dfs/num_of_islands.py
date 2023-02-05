from typing import List


class Solution:
    """
    https://leetcode.com/problems/number-of-islands/
    Given an m x n 2D binary grid which represents a map of '1's (land) and '0's (water),
    return the number of islands.

    An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically.
    You may assume all four edges of the grid are all surrounded by water.

    Input: grid = [
                  ["1","1","1","1","0"],
                  ["1","1","0","1","0"],
                  ["1","1","0","0","0"],
                  ["0","0","0","0","0"]
                ]
    Output: 1

    Input: grid = [
                  ["1","1","0","0","0"],
                  ["1","1","0","0","0"],
                  ["0","0","1","0","0"],
                  ["0","0","0","1","1"]
                ]
    Output: 3
    """
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        num_of_islands = 0

        for row, _ in enumerate(grid):
            for col, _ in enumerate(grid[row]):
                if grid[row][col] == "1":
                    num_of_islands += 1
                    self.dfs(grid, row, col)
        return num_of_islands

    def dfs(self, grid: List[List[str]], row, col):
        grid_row_len = len(grid)
        grid_col_len = len(grid[0])

        if row < 0 or col < 0 or row >= grid_row_len or col >= grid_col_len or grid[row][col] == "0":
            return

        grid[row][col] = "0"
        self.dfs(grid, row-1, col)
        self.dfs(grid, row+1, col)
        self.dfs(grid, row, col-1)
        self.dfs(grid, row, col+1)






if __name__ == '__main__':
    grid = [["1", "1", "1", "1", "0"],
            ["1", "1", "0", "1", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "0", "0", "0"]]
    solution = Solution()
    solution.numIslands(grid)

