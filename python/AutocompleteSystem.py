
from collections import defaultdict

class AutocompleteSystem(object):

    def __init__(self, sentences, times):
        """
        :type sentences: List[str]
        :type times: List[int]
        """
        self.prefix = defaultdict(list)
        self.count = defaultdict(int)

        n = len(sentences)
        for i in range(n):
            self.count[sentences[i]] = times[i]
            for j in range(1, len(sentences[i]) + 1):
                self.prefix[sentences[i][:j]].append(sentences[i])
        self.word = ''

    def input(self, c):
        """
        :type c: str
        :rtype: List[str]
        """
        if c == '#':
            if self.count.get(self.word, False) is False:
                for i in range(1, len(self.word) + 1):
                    self.prefix[self.word[:i]].append(self.word)
            self.count[self.word] += 1
            self.word = ''
            return []
        else:
            self.word += c
            if self.prefix.get(self.word, False) is False:
                return []
            else:
                # -self.count[s] for descend order, and second will use s to sort
                self.prefix[self.word].sort(key=lambda s: (-self.count[s], s))
                return self.prefix[self.word][:3]

# Your AutocompleteSystem object will be instantiated and called as such:
# obj = AutocompleteSystem(sentences, times)
# param_1 = obj.input(c)