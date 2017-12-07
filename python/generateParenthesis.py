class Solution:
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        result  = [['']]
        if n == 0:
            return result[-1]
        for i in range(1, n + 1):
            res = []
            for j in range(0, i):
                for first in result[j]:
                    for second in result[i - j - 1]:
                        res.append('(' + first + ')' + second)
                        
            result.append(res)
            
        return result[-1]