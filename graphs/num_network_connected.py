from typing import List


class Solution:
    def find(self, e, d_set):
        parent = e
        while d_set[parent] >= 0:
            parent = d_set[parent]
        return parent, d_set[parent]

    def union(self, e_x, edge_x, e_y, edge_y, d_set):
        if edge_x == edge_y or abs(edge_x) > abs(edge_y):
            temp_y = d_set[e_y]
            d_set[e_y] = e_x
            d_set[e_x] = -1 * (abs(d_set[e_x]) + abs(temp_y))
        else:  # edge_y > edge_x:
            temp_x = d_set[e_x]
            d_set[e_x] = e_y
            d_set[e_y] = -1 * (abs(d_set[e_y]) + abs(temp_x))

    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        cycles = 0
        if n - len(connections) >= 2:
            return -1
        d_set = [-1] * n
        for e in connections:
            x_idx, edge_x = self.find(e[0], d_set)
            y_idx, edge_y = self.find(e[1], d_set)
            if edge_x == edge_y and x_idx == y_idx:
                cycles += 1
            else:
                self.union(e[0], edge_x, e[1], edge_y, d_set)
        return cycles


if __name__ == '__main__':
    solution = Solution()
    r = solution.makeConnected(12, [[1,5],[1,7],[1,2],[1,4],[3,7],[4,7],[3,5],[0,6],[0,1],[0,4],[2,6],[0,3],[0,2]])
    assert r == 0

    solution = Solution()
    r = solution.makeConnected(5, [[0, 1], [0, 2], [3, 4], [2, 3]])
    assert r == 0

    solution = Solution()
    r = solution.makeConnected(6, [[0, 1], [0, 2], [0, 3], [1, 2]])
    assert r == -1

    solution = Solution()
    r = solution.makeConnected(6, [[0, 1], [0, 2], [0, 3], [1, 2], [1, 3]])
    assert r == 2

    solution = Solution()
    r = solution.makeConnected(4, [[0, 1], [0, 2], [1, 2]])
    assert r == 1
