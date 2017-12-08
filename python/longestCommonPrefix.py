class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        prefix = ''
        n = len(strs)
        if n == 0:
            return prefix

        str1 = strs[0]
        idx = len(str1)
        for i in range(1, n):
            s = strs[i]
            j = 0
            while j <= idx and j < len(str1) and j < len(s):
                if str1[j] != s[j]:
                    idx = min(idx, j)
                    break
                j += 1
            idx = min(idx, j)

        return str1[:idx]
