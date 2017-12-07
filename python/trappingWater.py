class Solution:
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        i = 0
        j = len(height) - 1
        res = 0
        cur_min = 0
        while (i < j):
            if (height[i] < height[j]):
                cur_min = max(cur_min, height[i])
                res += cur_min - height[i]
                i += 1

            elif (height[i] >= height[j]):
                cur_min = max(cur_min, height[j])
                res += cur_min - height[j]
                j -= 1

        return res
