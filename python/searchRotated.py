class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        return self.binary(nums, 0, len(nums) - 1, target)

    def binary(self, nums, i, j, target):
        if i == j:
            if nums[i] == target:
                return i
            else:
                return -1

        elif i < j:

            mid = (i + j) // 2
            if nums[mid] == target:
                return mid
            if nums[i] <= nums[mid]:
                if target >= nums[i] and target < nums[mid]:
                    return self.binary(nums, i, mid - 1, target)
                else:
                    return self.binary(nums, mid + 1, j, target)

            else:
                if target > nums[mid] and target <= nums[j]:
                    return self.binary(nums, mid + 1, j, target)
                else:
                    return self.binary(nums, i, mid - 1, target)
        else:
            return -1
