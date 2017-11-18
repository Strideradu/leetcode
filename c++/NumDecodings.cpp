class Solution {
public:
    int numDecodings(string s) {
        //DP: dp[i] is the comnination for message end at i
        int n = s.size();
        if (n == 0) return 0;
        vector<int> result(n + 1, 0);
        result[0] = 1;
        
        for (int i = 1; i <= n; i ++){
            if (isValid(s[i - 1])){
                result[i] += result[i - 1];
            }
            if (i >1 && isValid(s[i - 2], s[i - 1])){
                result[i] += result[i - 2];
            }
            else if (!(isValid(s[i - 1]))){
                return 0;
            }
        }
        
        return result[n];
    }
    
    bool isValid(char a,char b){
        return a == '1'||(a == '2' && b <='6');
    }
    bool isValid(char a){
        return a != '0';
    }
};