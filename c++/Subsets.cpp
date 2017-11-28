class Solution {
public:
    vector<vector<int>> subsets(vector<int>& nums) {
        vector<vector<int>> result(1, vector<int>());
        int n = nums.size();
        for(int i = 0; i < n; i ++){
            int m = result.size();
            for(int j = 0; j<m; j ++){
                result.push_back(result[j]);
                result.back().push_back(nums[i]);
            }
        }
        return result;
    }
};