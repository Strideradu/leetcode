class Solution:
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        left = 0
        right = 0
        result = set()
        # record extra ( and )
        for char in s:
            if char == '(':
                left += 1

            elif char == ')':
                if left > 0:
                    left -= 1
                else:
                    right += 1

        self.dfs(s, 0, left, right, 0, "", result)
        return list(result)

    def dfs(self, s, index, left, right, pair, path, res):
        n = len(s)
        if index == n:
            if left == 0 and right == 0 and pair == 0:
                res.add(path)
            return

        if s[index] != '(' and s[index] != ')':
            self.dfs(s, index + 1, left, right, pair, path + s[index], res)

        elif s[index] == '(':
            if left > 0:
                self.dfs(s, index + 1, left - 1, right, pair, path, res)
            # in this situation we should not add 1 for left, as right is fro extra ()
            self.dfs(s, index + 1, left, right, pair + 1, path + s[index], res)

        elif s[index] == ')':
            if right > 0:
                self.dfs(s, index + 1, left, right - 1, pair, path, res)
            if pair > 0:
                # in this situation we should not minus 1 for right, as right is fro extra )
                self.dfs(s, index + 1, left, right,
                         pair - 1, path + s[index], res)

        return
