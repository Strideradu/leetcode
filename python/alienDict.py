class Solution:
    def alienOrder(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        pre = collections.defaultdict(set)
        suc = collections.defaultdict(set)
        for i in range(len(words) - 1):
            idx = 0
            word = words[i]
            succ = words[i + 1]
            while idx < len(word) and idx < len(succ):
                if word[idx] != succ[idx]:
                    pre[succ[idx]].add(word[idx])
                    suc[word[idx]].add(succ[idx])
                    break

                idx += 1

        chars = set(''.join(words))
        queue = collections.deque([])
        for char in chars:
            if char not in pre:
                queue.append(char)
        visited = set()
        result = ''
        while(queue):
            cur = queue.popleft()
            if cur not in visited:
                visited.add(cur)
                result += cur
                for successor in suc[cur]:
                    pre[successor].remove(cur)
                    if len(pre[successor]) == 0:
                        queue.append(successor)
        if len(result) == len(chars):
            return result
        else:
            return ''
