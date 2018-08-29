class Solution:
    def hitBricks(self, grid, hits):
        """
        :type grid: List[List[int]]
        :type hits: List[List[int]]
        :rtype: List[int]
        """
        m = len(grid)
        n = len(grid[0])

        def dfs(x, y):
            if not (0 <= x < m and 0 <= y < n) or grid[x][y] != 1:
                return 0
            result = 1
            grid[x][y] = 2
            for i, j in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
                result += dfs(i, j)

            return result

        def is_connected(x, y):
            return x == 0 or any([0 <= i < m and 0 <= j < n and grid[i][j] == 2 for i, j in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]])

        for i, j in hits:
            grid[i][j] -= 1

        for j in range(n):
            dfs(0, j)

        result = [0] * len(hits)
        for k in reversed(range(len(hits))):
            i, j = hits[k]
            grid[i][j] += 1
            if grid[i][j] == 1 and is_connected(i, j):
                result[k] = dfs(i, j) - 1

        return result
