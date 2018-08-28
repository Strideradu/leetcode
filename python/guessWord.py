# """
# This is Master's API interface.
# You should not implement it, or speculate about its implementation
# """
# class Master:
#    def guess(self, word):
#        """
#        :type word: str
#        :rtype int
#        """


class Solution:
    def numOfMatch(self, word1, word2):
        match = 0
        for i in range(len(word1)):
            if word1[i] == word2[i]:
                match += 1
        return match

    def findSecretWord(self, wordlist, master):
        """
        :type wordlist: List[Str]
        :type master: Master
        :rtype: None
        """
        word = wordlist[0]
        space = wordlist.copy()
        space.remove(word)
        test = master.guess(word)
        while test != 6:
            new_space = set()
            for candidate in space:
                if self.numOfMatch(word, candidate) == test:
                    new_space.add(candidate)
            space = new_space
            word = space.pop()
            test = master.guess(word)
