// Forward declaration of isBadVersion API.
bool isBadVersion(int version);

class Solution {
public:
    int firstBadVersion(int n) {
        if (n == 0) return 0;
        return helper(1, n);
    }
    
    int helper(long start, long end){
        if (start == end){
            return start;
        }
        long middle = (start + end)/2;
        if (isBadVersion(middle)){
            return helper(start, middle);
        }
        else{
            return helper(middle+1, end);
        }
    }
};