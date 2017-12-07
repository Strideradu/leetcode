class Solution:
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        n = len(nums)
        dp = [collections.defaultdict(int) for i in range(n + 1)]
        dp[0][0] = 1
        for i in range(n):
            for j in dp[i].keys():
                dp[i + 1][j + nums[i]] += dp[i][j]
                dp[i + 1][j - nums[i]] += dp[i][j]

        return dp[n][S]
