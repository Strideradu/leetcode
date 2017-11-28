class Solution:
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        length = len(s)
        if length < 1 or s[0] == '0':
            return 0
        dp = [0] * (length + 1)
        dp[0] = dp[1] = 1
        for i in range(2, length + 1):
            if s[i - 1] != '0':
                dp[i] += dp[i - 1]

            if (s[i - 2] == '1') or (s[i - 2] == '2' and int(s[i - 1]) <= 6):
                dp[i] += dp[i - 2]

        return dp[length]


class Solution:
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        mod = 1000000007
        length = len(s)
        if length < 1 or s[0] == '0':
            return 0
        dp = [0] * (length + 1)
        dp[0] = 1
        if s[0] == '*':
            dp[1] = 9
        else:
            dp[1] = 1
        for i in range(2, length + 1):
            if s[i - 1] == '*' or s[i - 2] == '*':
                if s[i - 1] == '*' and s[i - 2] == '*':
                    dp[i] = dp[i - 1] * 9 + dp[i - 2] * 15
                elif s[i - 1] == '*':
                    dp[i] += dp[i - 1] * 9
                    if s[i - 2] == '1':
                        dp[i] += dp[i - 2] * 9
                    elif s[i - 2] == '2':
                        dp[i] += dp[i - 2] * 6
                elif s[i - 2] == "*":
                    if s[i - 1] != '0':
                        dp[i] += dp[i - 1]
                    if int(s[i - 1]) <= 6:
                        dp[i] += dp[i - 2] * 2
                    else:
                        dp[i] += dp[i - 2]

            else:
                if s[i - 1] != '0':
                    dp[i] += dp[i - 1]

                if (s[i - 2] == '1') or (s[i - 2] == '2' and int(s[i - 1]) <= 6):
                    dp[i] += dp[i - 2]

            dp[i] = dp[i] % mod

        return dp[length]
