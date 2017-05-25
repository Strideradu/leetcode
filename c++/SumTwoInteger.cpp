class Solution {
public:
    int getSum(int a, int b) {
        int sum = a;
        
        while (b != 0){
            sum = a ^ b; // XOR will return at that position the sum of a and b, except 1 + 1 = 0
            b = (a & b) << 1; // a&b only be 1 when a = 1 and b =1 ,so can be used as carry, << move left 1 bit
            a = sum;
        }
        
        return sum;
    }
};