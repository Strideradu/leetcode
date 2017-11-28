class Solution:
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        dp = [0] * (target + 1)
        dp[0] = 1
        nums.sort()
        for i in range(1, target + 1):
            for num in nums:
                if num > i:
                    break
                elif num == i:
                    dp[i] += 1
                else:
                    dp[i] += dp[i - num]

        return dp[target]
