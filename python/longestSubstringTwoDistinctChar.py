import collections
class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s):
        """
        :type s: str
        :rtype: int
        """
        occ = collections.defaultdict(int)
        n = len(s)
        left = 0
        length = 0
        count = 0
        for i in range(n):
            occ[s[i]] += 1
            if occ[s[i]] == 1:
                count += 1
                while count > 2:
                    occ[s[left]] -= 1
                    if occ[s[left]] == 0:
                        count -= 1

                    left += 1
            length = max(length, i - left + 1)

        return length
