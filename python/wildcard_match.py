class Solution:
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        m = len(s) + 1
        n = len(p) + 1
        dp = [[False for i in range(n)] for j in range(m)]

        for i in range(n - 1):
            if p[i] == '*':
                dp[0][i + 1] = True
            else:
                break
        dp[0][0] = True
        for i in range(1, m):
            for j in range(1, n):
                if s[i - 1] == p[j - 1] or p[j - 1] == '?':
                    dp[i][j] = dp[i - 1][j - 1]

                if p[j - 1] == '*':
                    dp[i][j] = (dp[i - 1][j] or dp[i - 1]
                                [j - 1] or dp[i][j - 1])
        return dp[m - 1][n - 1]
