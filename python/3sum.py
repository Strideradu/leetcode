class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        n = len(nums)
        result = []
        for i, num in enumerate(nums):
            if num <= 0:
                if i == 0 or nums[i - 1] != num:
                    target = -num
                    left = i + 1
                    right = n - 1
                    while(left < right):
                        if nums[left] + nums[right] == target:
                            ans = [num, nums[left], nums[right]]
                            result.append(ans)
                            while (left < right and nums[left] == ans[1]):
                                left += 1

                            while (left < right and nums[right] == ans[2]):
                                right -= 1

                        elif nums[left] + nums[right] < target:
                            left += 1
                        elif nums[left] + nums[right] > target:
                            right -= 1

        return result
