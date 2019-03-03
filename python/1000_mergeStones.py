class Solution:
    def mergeStones(self, stones: List[int], K: int) -> int:
        num = len(stones)

        if (num - 1) % (K - 1) != 0:
            return -1

        pre_sum = [0 for i in range(num + 1)]
        dp = [[[float('inf') for i in range(num + 1)]
               for j in range(num + 1)] for k in range(num + 1)]
        for i in range(1, num + 1):
            pre_sum[i] = pre_sum[i - 1] + stones[i - 1]
            dp[i][i][1] = 0

        # k: the number of tiles going to be merged
        for k in range(1, num + 1):
            for i in range(1, num - k + 2):
                j = i + k - 1
                for size in range(2, k + 1):
                    for mid in range(i, j):
                        dp[i][j][size] = min(
                            dp[i][j][size], dp[i][mid][size - 1] + dp[mid + 1][j][1])

                    dp[i][j][1] = min(dp[i][j][1], dp[i][j]
                                      [K] + pre_sum[j] - pre_sum[i - 1])

        return dp[1][num][1]
