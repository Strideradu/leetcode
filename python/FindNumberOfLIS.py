class Solution(object):
    def findNumberOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        len_array = len(nums)
        if len_array == 0:
            return 0
        length = [0] * len_array
        count = [0] * len_array
        
        for i in range(len_array):
            new_count = 1
            new_length = 1
            for j in range(i):
                if nums[j] < nums[i]:
                    if length[j] + 1 > new_length:
                        new_length = length[j] + 1
                        new_count = count[j]
                    elif length[j] + 1 == new_length:
                        new_count += count[j]
            
            length[i] =  new_length
            count[i] = new_count
        max_len = max(length)
        max_count = 0
        for i in range(len_array):
            if length[i] == max_len:
                max_count += count[i]
        return max_count