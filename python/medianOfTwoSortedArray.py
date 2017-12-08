class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        m = len(nums1)
        n = len(nums2)
        if m > n:
            return self.findMedianSortedArrays(nums2, nums1)

        imin = 0
        imax = m
        # extra 1 so that the result for odd will be directly get
        k = (m + n + 1) // 2
        while (imin <= imax):
            i = (imin + imax) // 2
            j = k - i

            if i < m and nums1[i] < nums2[j - 1]:
                imin = i + 1

            elif i > 0 and nums1[i - 1] > nums2[j]:
                imax = i - 1

            else:

                if i == 0:
                    max_left = nums2[j - 1]
                elif j == 0:
                    max_left = nums1[i - 1]
                else:
                    max_left = max(nums1[i - 1], nums2[j - 1])

                if (m + n) % 2 == 1:
                    return max_left

                if i == m:
                    min_right = nums2[j]

                elif j == n:
                    min_right = nums1[i]
                else:
                    min_right = min(nums1[i], nums2[j])

                return (max_left + min_right) / 2
