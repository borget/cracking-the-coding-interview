from typing import List


class Solution:
    def get_max(self, collection):
        return max((len(v), k) for k, v in collection.items())

    def road(self, city_roads, city_a, city_b):
        if city_a in city_roads:
            city_roads[city_a].add(city_b)
        else:
            city_roads[city_a] = set()
            city_roads[city_a].add(city_b)

    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        city_roads = dict()
        for road in roads:
            city_a = road[0]
            city_b = road[1]
            self.road(city_roads, city_a, city_b)
            self.road(city_roads, city_b, city_a)
        x, y = self.get_max(city_roads)
        max_v = city_roads[y]
        del city_roads[y]
        max_result = len(max_v)
        for c in city_roads:
            union = max_v.union(city_roads[c])
            if c in union and y in union:
                union.remove(c)
            if len(union) > max_result:
                max_result = len(union)
        return max_result


if __name__ == '__main__':
    s = Solution()
    r = s.maximalNetworkRank(n=4, roads=[[0, 1], [0, 3], [1, 2], [1, 3]])
    assert r == 4

    s = Solution()
    r = s.maximalNetworkRank(6, [[0, 3], [0, 1], [0, 2], [4, 5], [0, 4]])
    assert r == 5



    s = Solution()
    r = s.maximalNetworkRank(n=5, roads=[[0, 1], [0, 3], [1, 2], [1, 3], [2, 3], [2, 4]])
    assert r == 5

    s = Solution()
    r = s.maximalNetworkRank(n=8, roads=[[0, 1], [1, 2], [2, 3], [2, 4], [5, 6], [5, 7]])
    assert r == 5
