class Solution:
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        count = dict(collections.Counter(t))
        need = len(t)
        j = 0
        window = len(s) + 1
        start = 0
        end = 0
        for i, char in enumerate(s):
            
            if char in count:
                count[char] -= 1
                if count[char] >= 0:
                    need -= 1
                    while(need == 0):
                        if (i - j) < window:
                            print(window)
                            window = i - j
                            start = j
                            end = i
                        if s[j] in count:                            
                            if count[s[j]] == 0:
                                need += 1
                            count[s[j]] += 1
                        j += 1

        if window == len(s)+1:
            return ""
        else:
            return s[start:end + 1]