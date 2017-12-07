class Solution:
    def palindromePairs(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """
        result = []
        d = {}
        for idx, word in enumerate(words):
            d[word] = idx

        for idx, word in enumerate(words):
            n = len(word)
            for i in range(n + 1):
                pre = word[:i]
                suf = word[i:]
                if self.isPalindrome(pre):
                    sur_rev = suf[::-1]
                    if sur_rev in d:
                        if sur_rev != word:
                            result.append([d[sur_rev], idx])

                # i != n to make sure no duplicate
                if i != n and self.isPalindrome(suf):
                    pre_rev = pre[::-1]
                    if pre_rev in d:
                        if pre_rev != word:
                            result.append([idx, d[pre_rev]])

        return result

    def isPalindrome(self, word):
        return word == word[::-1]
