class Solution:
    def totalHammingDistance(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        """
        So, let's consider the i-th column, which consists of numbers chosen from {0, 1}. The total hamming distance would be the number of 
        pairs of numbers that are different. That is,

        Total hamming distance for the i-th bit =(the number of zeros in the i-th position) * (the number of ones in the i-th position)
        """
        bits = [[0, 0] for _ in range(32)]
        for x in nums:
            for i in range(32):
                bits[i][x % 2] += 1
                x //= 2
        return sum(x * y for x, y in bits)
