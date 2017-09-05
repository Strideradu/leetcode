class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        int n = nums.size();
        vector<int> res(n, 1);
        int prefix = 1, suffix = 1;
        for (int i = 0; i < n; i ++)
        {
            res[i] *= prefix;
            prefix *= nums[i];
            res[n - i -1] *= suffix;
            suffix *= nums[n-i-1];
            
        }
        
        return res;
        
    }
};