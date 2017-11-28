class Solution {
public:
    bool checkSubarraySum(vector<int>& nums, int k) {
        map<int, int> mp;
        
        // dealing with corner case: have two 0
        mp[0] = -1;
        
        int sum = 0;
        int n = nums.size();
        for (int i = 0; i < n; i ++){
            sum += nums[i];
            if (k!=0) sum = sum % k;
            //int times = sum/k;
            if (mp.find(sum)!=mp.end()){
                if (i - mp[sum] > 1){
                    return true;
                }
            }
            else{
                mp[sum] = i;
            }
        }
        
        return false;
    }
};