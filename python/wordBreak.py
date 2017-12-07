class Solution:
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        words = set(wordDict)
        n = len(s)
        dp = [False for i in range(n + 1)]
        dp[0] = True
        for i in range(n):
            for j in range(i, -1, -1):
                if dp[j]:
                    if s[j: i + 1] in words:
                        dp[i + 1] = True
                        break

        return dp[n]
