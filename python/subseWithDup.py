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


class Solution:
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        result = [[]]
        for i, num in enumerate(nums):
            if i == 0 or nums[i] != nums[i - 1]:
                l = len(result)
            for j in range(len(result) - l, len(result)):
                result.append(result[j] + [nums[i]])

        return result
