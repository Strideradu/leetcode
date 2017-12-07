class Node:
    def __init__(self, char):
        self.val = char
        self.child = {}
        self.isEnd = False


class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = Node("")

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: void
        """
        cur = self.root
        for c in word:
            if not c in cur.child:
                cur.child[c] = Node(c)
            cur = cur.child[c]
        cur.isEnd = True

    def search(self, word):
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        return self._search(word, self.root)

    def _search(self, word, node):
        if len(word) == 0:
            return node.isEnd

        c = word[0]
        if c != '.':
            if not c in node.child:
                return False
            return self._search(word[1:], node.child[c])
        else:
            for c in node.child:
                if self._search(word[1:], node.child[c]):
                    return True
            return False


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
