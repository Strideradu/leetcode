class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer[]}
    def twoSum(self, nums, target):
        dict_index = {}
        for i, num  in enumerate(nums):
            
            complement = dict_index.get(target-num)
            if  complement!= None:
                return [complement, i]
                
            else:
                dict_index[num] = i