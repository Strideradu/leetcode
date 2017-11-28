class Solution:
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        dict = {'0': '', '1': '', '2': 'abc', '3': 'def', '4': 'ghi',
                '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        if len(digits) == 0:
            return []
        result = [['']]
        for digit in digits:
            new_res = []
            for c in dict[digit]:
                for res in result[-1]:
                    new_res.append(res + c)

            result.append(new_res)
        return result[-1]
