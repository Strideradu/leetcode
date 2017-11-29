class Solution:
    def groupStrings(self, strings):
        """
        :type strings: List[str]
        :rtype: List[List[str]]
        """
        groups = collections.defaultdict(list)
        for s in strings:
            val = []
            for char in s:
                val.append((ord(char) - ord(s[0]))%26)
            groups[tuple(val)].append(s)
            
        result = []
        for key, value in groups.items():
            result.append(value)
            
        return result