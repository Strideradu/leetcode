class Solution {
public:
    int search(vector<int>& nums, int target) {
        int n = nums.size();
        if (n == 0) return -1;
        int left = 0, right = n - 1;
        while(left < right){
            int center = (left + right)/2;
            cout << center <<endl;
            if (nums[center] == target) return center;
            
            // divide here will round down, so we need include equal for left, center compare
            if (nums[left] <= nums[center]){
                if (nums[left]<=target&& target<nums[center]){
                    right = center - 1;
                }
                else{
                    left = center + 1;
                }
            }
            else{
                if (nums[center] < target && target <= nums[right]){
                    left = center + 1;
                }
                else{
                    right = center - 1;
                }
            }
        }
        return nums[left] == target ? left : -1;
    }
};