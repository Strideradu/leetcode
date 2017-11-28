from collections import deque, Counter

class Solution:
    
    
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        chars = 'abcdefghijklmnopqrstuvwxyz'
        count = Counter(wordList)
        if count[endWord] == 0:
            return 0
        queue = deque()
        queue.append((beginWord, 1))
        visited = set()
        while queue:
            word, steps = queue.popleft()
            if not word in visited:
                visited.add(word)
                if word == endWord:
                    return steps
                for i in range(len(word)):
                    for char in chars:
                        new_word = word[:i] + char + word[i+1:]
                        if count[new_word] != 0:
                            queue.append((new_word, steps + 1))
                            
        return 0