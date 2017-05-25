class Solution {
public:
    int romanToInt(string s) {
        int result = 0, last = 0;
        int digit;
        for (int i = s.size() -1; i >=0; i --){
            switch(s[i]){
                case 'I': digit = 1; break;
                case 'V': digit = 5; break;
                case 'X': digit = 10; break;
                case 'L': digit = 50; break;
                case 'C': digit = 100; break;
                case 'D': digit = 500; break;
                case 'M': digit = 1000; break;
            }
            
            if (digit >= last){
                result += digit;
                last = digit;
            }
            else {
                result -= digit;
            }
        }
        return result;
    }
};