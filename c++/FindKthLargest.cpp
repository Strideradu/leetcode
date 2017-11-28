class Solution {
public:
    int findKthLargest(vector<int>& nums, int k) {
        int left = 0, right = nums.size() - 1;
        while(true){
            int pos = partition(nums, left, right);
            if (pos == k-1) return nums[pos];
            if (pos > k-1) right = pos - 1;
            else left = pos + 1;
        }
    }
    
    int partition(vector<int>& nums, int left, int right){
        int pivot = nums[left];
        int l = left+1, r = right;
        while(l<=r){
            // this need to be first condition other wise we may need use continue to avoid stay in same while 
            if (nums[l]<pivot && nums[r]>pivot){
                swap(nums[l], nums[r]);
                l++;
                r--;
            }
            if (nums[l] >= pivot) l++;
            if (nums[r] <= pivot) r--;
                       
        }
        swap(nums[left], nums[r]);
        return r;
    }
};

class Solution {
public:
    int findKthLargest(vector<int>& nums, int k) {
        priority_queue<int, vector<int>, greater<int>> Q;
        int n = nums.size();
        for (int i = 0; i < n; i++) {
            if (i < k) {
                Q.push(nums[i]);
            }
            else {
                if(Q.top() <= nums[i]) {
                    Q.push(nums[i]);
                    Q.pop();
                }
            }
        }
        return Q.top();
    }
};