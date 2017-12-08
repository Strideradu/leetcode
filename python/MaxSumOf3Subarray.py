class Solution:
    def maxSumOfThreeSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        n = len(nums)
        sums = [0]
        s = 0
        for i in range(n):
            s += nums[i]
            sums.append(s)
        s_max = 0
        right = [0 for i in range(n - k + 1)]
        for i in range(n - k, -1, -1):
            s = sums[i + k] - sums[i]
            if s > s_max:
                s_max = s
                right[i] = i
            else:
                right[i] = right[i + 1]
        s_max = 0
        left = [0 for i in range(n)]
        for i in range(k - 1, n):
            s = sums[i + 1] - sums[i - k + 1]
            if s > s_max:
                s_max = s
                left[i] = i
            else:
                left[i] = left[i - 1]

        s_max = 0
        result = [-1, -1, -1]
        for i in range(k, n - 2 * k + 1):
            l = left[i - 1]
            r = right[i + k]
            s = sums[i + k] - sums[i] + sums[l + 1] - \
                sums[l - k + 1] + sums[r + k] - sums[r]
            if s > s_max:
                s_max = s
                result[0] = l - k + 1
                result[1] = i
                result[2] = r

        return result
