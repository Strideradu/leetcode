class Solution:
    def addOperators(self, num, target):
        """
        :type num: str
        :type target: int
        :rtype: List[str]
        """
        self.result = set()
        n = len(num)
        for i in range(1, n + 1):
            if i == 1 or num[0] != '0':
                self.dfs(num, i, num[:i], int(num[:i]), int(num[:i]), target)

        return list(self.result)

    def dfs(self, num, pos, path, res, last, target):
        n = len(num)
        if pos == n and res == target:
            self.result.add(path)
            return
        for i in range(pos + 1, n + 1):
            nb = int(num[pos:i])
            if i == pos + 1 or num[pos] != '0':
                self.dfs(num, i, path + '+' + num[pos:i], res + nb, nb, target)
                self.dfs(num, i, path + '-' +
                         num[pos:i], res - nb, -nb, target)
                self.dfs(num, i, path + '*' +
                         num[pos:i], res - last + last * nb, last * nb, target)
