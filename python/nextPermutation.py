class Solution:
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        i = n - 1
        while i > 0 and nums[i - 1] >= nums[i]:
            i -= 1
        if i == 0:
            nums[0:n] = nums[0:n][::-1]

        else:
            pivot = i - 1
            i = n - 1
            while i > pivot and nums[i] <= nums[pivot]:
                i -= 1
            nums[i], nums[pivot] = nums[pivot], nums[i]
            nums[pivot + 1: n] = nums[pivot + 1: n][::-1]
