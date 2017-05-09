class Solution {
public:
    int singleNumber(vector<int>& nums) {
        int result = nums[0];
        int i = 1, len = nums.size();
        for (i; i < len; i ++){
            result = result^nums[i];
        }
        return result;
    }
};