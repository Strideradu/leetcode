class Solution:
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = [[]]
        for num in nums:
            n = len(result)
            for i in range(n):
                res = result[i]
                new = res + [num]
                result.append(new)

        return result


from collections import Counter


class Solution:
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        c = Counter(nums)
        unique = list(c)
        result = [[]]
        for i, num in enumerate(unique):
            for j in range(len(result)):
                repeat = c[num]
                for k in range(repeat):
                    result.append(result[j] + (k + 1) * [unique[i]])

        return result
