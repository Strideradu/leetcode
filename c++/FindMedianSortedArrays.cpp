class Solution {
public:
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
        int l1 = nums1.size();
        int l2 = nums2.size();
        if (l1 < l2) return findMedianSortedArrays(nums2, nums1);	// Make sure A2 is the shorter one.
        
        if (l2 == 0) return ((double)nums1[(l1-1)/2] + (double)nums1[l1/2])/2;  // If A2 is empty
        int start = 0, end = 2*l2, half = l1 + l2;
        while (start <= end){
            int mid2 = (start + end)/2;
            int mid1 = half - mid2;
            
            double L1 = (mid1 == 0) ? INT_MIN : nums1[(mid1-1)/2];	// Get L1, R1, L2, R2 respectively
            double L2 = (mid2 == 0) ? INT_MIN : nums2[(mid2-1)/2];
            double R1 = (mid1 == l1 * 2) ? INT_MAX : nums1[(mid1)/2];
            double R2 = (mid2 == l2 * 2) ? INT_MAX : nums2[(mid2)/2];
            
            if (L1 > R2) start = mid2 + 1;
            else if (L2 > R1) end = mid2 - 1;
            else return (max(L1,L2) + min(R1, R2)) / 2;
        }
    }
};