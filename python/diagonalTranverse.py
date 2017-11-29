class Solution:
    def findDiagonalOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        result = []
        m = len(matrix)
        if m == 0:
            return []
        n = len(matrix[0])
        for i in range(m + n - 1):

            high = min(i + 1, m)
            low = max(0, i + 1 - n)
            if i % 2 == 1:
                for x in range(low, high):
                    print(matrix[x][i - x])
                    result.append(matrix[x][i - x])

            else:
                for x in range(high - 1, low - 1, -1):
                    print(matrix[x][i - x])
                    result.append(matrix[x][i - x])

        return result
