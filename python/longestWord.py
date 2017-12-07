class Solution:
    def longestWord(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        words.sort()
        build = {}
        result = None
        for word in words:
            if len(word) == 1 or word[:-1] in build:
                build[word] = True
                if result is None or len(word)>len(result):
                    result = word
                    
        return result