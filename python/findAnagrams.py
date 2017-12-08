class Solution:
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        m = len(s)
        n = len(p)
        count = dict(collections.Counter(p))
        total = n
        scount = {}
        result = []
        for i in range(m):
            if s[i] not in scount:
                scount[s[i]] = 0
            scount[s[i]] += 1
            if scount == count:
                result.append(i - n + 1)
            if i >= n - 1:
                scount[s[i - n + 1]] -= 1
                if scount[s[i - n + 1]] <= 0:
                    scount.pop(s[i - n + 1])

        return result
