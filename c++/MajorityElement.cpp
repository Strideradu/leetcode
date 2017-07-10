class Solution {
public:
    int majorityElement(vector<int>& nums) {
        int major=0, count = 0;
        
        for(int n: nums){
            if (major == n){
                count++;
            }
            else if(count == 0) {
                count=1;
                major = n;
            }
            else {
                count--;
            }
        }
        
        return major;
    }
};