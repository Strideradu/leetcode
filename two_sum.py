class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer[]}
    def twoSum(self, nums, target):
        dict_index={}
        for i in range(len(nums)):
            if nums[i] in dict_index:
                dict_index[nums[i]].append(i+1)
            else:
                dict_index[nums[i]]=[i+1]
        for num in dict_index:
            if (target - num) in dict_index:
                for index1 in dict_index[num]:
                    for index2 in dict_index[target-num]:
                        if index1 < index2:
                            return index1, index2
                        elif index1 > index2:
                            return index2, index1
