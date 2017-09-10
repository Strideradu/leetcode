class MagicDictionary(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        # use length as key!
        self.dict = {}

    def buildDict(self, dict):
        """
        Build a dictionary through a list of words
        :type dict: List[str]
        :rtype: void
        """
        for word in dict:
            length = len(word)
            if self.dict.get(length, False) is False:
                self.dict[length] = [word]
            else:
                self.dict[length].append(word)

    def search(self, word):
        """
        Returns if there is any word in the trie that equals to the given word after modifying exactly one character
        :type word: str
        :rtype: bool
        """
        
        length =  len(word)
        # print(length)
        if self.dict.get(length, False) is False:
            return False
        else:
            word_list = self.dict[length]
            for search_word in word_list:
                mismatch = 0
                for i in range(length):
                    if word[i] != search_word[i]:
                        mismatch += 1
                    
                if mismatch == 1:
                    return True
            return False
        


# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dict)
# param_2 = obj.search(word)