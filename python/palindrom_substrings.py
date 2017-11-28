class Solution:
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        length = len(s)
        ans = 0
        # there are 2*N + 1 possibble center of palindrom
        for center in range(2 * length + 1):
            left = center // 2
            right = left + center % 2
            while left >= 0 and right < length and s[left] == s[right]:
                ans += 1
                left -= 1
                right += 1

        return ans
