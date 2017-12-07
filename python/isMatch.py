class Solution:
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        m = len(s)
        n = len(p)
        dp = [[False for col in range(n + 1)] for row in range(m + 1)]
        dp[0][0] = True
        for i in range(0, m + 1):
            for j in range(1, n + 1):
                if p[j - 1] == '*':
                    dp[i][j] = (i > 0 and (s[i - 1] == p[j - 2] or p[j - 2]
                                           == '.') and dp[i - 1][j]) or dp[i][j - 2]

                elif p[j - 1] == '.':
                    dp[i][j] = (i > 0) and dp[i - 1][j - 1]

                elif i > 0 and s[i - 1] == p[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]

        return dp[m][n]
