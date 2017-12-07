class Solution:
    def __init__(self):
        self.result = set()

    def addOperators(self, num, target):
        """
        :type num: str
        :type target: int
        :rtype: List[str]
        """
        n = len(num)
        for i in range(1, n + 1):
            if i == 1 or num[0] != '0':
                self.dfs(num, i, int(num[0:i]),
                         num[0:i], int(num[0:i]), target)

        return list(self.result)

    def dfs(self, num, index, res, path, last, target):
        n = len(num)
        if index >= n:
            if res == target:
                self.result.add(path)

            return

        for i in range(1, n - index + 1):
            if i == 1 or num[index] != '0':
                cur = int(num[index:index + i])
                cur_str = num[index: index + i]
                self.dfs(num, index + i, res + cur,
                         path + '+' + cur_str, cur, target)
                self.dfs(num, index + i, res - cur, path +
                         '-' + cur_str, -cur, target)
                self.dfs(num, index + i, res - last + last * cur,
                         path + '*' + cur_str, last * cur, target)
