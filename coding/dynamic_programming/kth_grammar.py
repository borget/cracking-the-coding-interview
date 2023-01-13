# 1 0
# 2 01
# 3 [01,                                10]
# 4 0110                              1001
# 5 01101001                          10010110
# 6 0110100110010110                  1001011001101001
# 7 01101001100101101001011001101001  10010110011010010110100110010110
# 8 01101001100101101001011001101001  10010110011010010110100110010110 1001011001101001011010011001011001101001100101101001011001101001
class Solution:
    def get_kth(self, K, cache):
        len_cache0 = len(cache[0])
        if 0 <= K <= len_cache0:
            return cache[0][K - 1]
        elif len_cache0 < K <= len_cache0 + len_cache0:
            return cache[1][(K - len_cache0) - 1]

    def kthGrammar(self, N: int, K: int) -> int:
        cache = {3: ['01', '10']}
        if N == 1:
            return 0
        elif N == 2:
            return [0, 1][K - 1]
        elif N >= 4:
            for n in range(3, N):
                pos1 = cache[n][0] + cache[n][1]
                pos2 = cache[n][1] + cache[n][0]
                cache[n + 1] = [pos1, pos2]
        return self.get_kth(K, cache[N])


if __name__ == '__main__':


    s = Solution()
    result = s.kthGrammar(30, 434991989)
    print(result)
