from collections import defaultdict

class Solution:

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.index = defaultdict(list)
        for i, num in enumerate(nums):
            self.index[num].append(i)
        

    def pick(self, target):
        """
        :type target: int
        :rtype: int
        """
        return random.choice(self.index[target])
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)